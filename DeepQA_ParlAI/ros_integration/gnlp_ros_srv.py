import os
import logging

import asyncio
import websockets
import json as json

import pdb


# from chatbot import chatbot

async def service_callback():
    async with websockets.connect('ws://localhost:9090') as websocket:

        # advertise the service
        await websocket.send("{ \"op\": \"advertise_service\",\
                      \"type\": \"roboy_communication_cognition/GenerateAnswer\",\
                      \"service\": \"/roboy/cognition/generative_nlp/answer\"\
                    }")

        i = 1  # counter for the service request IDs

        #### prepare the model ####
        from parlai.core.agents import create_agent
        # from parlai.core.ROS_worlds import create_task
        from ROS_worlds import create_task

        opt = {'task': None, 'download_path': '/home/christoph/Documents/Roboy/ParlAI/downloads', \
               'datatype': 'train', 'image_mode': 'raw', 'numthreads': 1, 'hide_labels': False, 'batchsize': 1, \
               'include_labels': True, 'datapath': '/home/christoph/Documents/Roboy/ParlAI/data', \
               'model': 'projects.personachat.persona_seq2seq:PersonachatSeqseqAgentSplit', \
               'model_file': '/home/christoph/Documents/Roboy/ParlAI/data/models/convai2/profilememory/profilememory_convai2_model', \
               'dict_class': None, 'display_examples': False, 'image_size': 256, 'image_cropsize': 224, \
               'dict_file': '/home/christoph/Documents/Roboy/ParlAI/data/models/convai2/profilememory/profilememory_convai2.dict', \
               'dict_initpath': None, 'dict_language': 'english', 'dict_max_ngram_size': -1, 'dict_minfreq': 0, \
               'dict_maxtokens': -1, 'dict_nulltoken': '__NULL__', 'dict_starttoken': '__START__',
               'dict_endtoken': '__END__', \
               'dict_unktoken': '__UNK__', 'dict_tokenizer': 'split', 'dict_lower': False, 'hiddensize': 1024, \
               'embeddingsize': 300, 'numlayers': 2, 'learningrate': 0.5, 'dropout': 0.1, 'bidirectional': False, \
               'attention': None, 'no_cuda': False, 'gpu': -1, 'rank_candidates': False, 'truncate': 100,
               'encoder': 'lstm', \
               'decoder': 'same', 'optimizer': 'adam', 'personachat_useprevdialog': False,
               'personachat_printattn': False, \
               'personachat_attnsentlevel': False, 'personachat_sharelt': False, 'personachat_reweight': None, \
               'personachat_guidesoftmax': False, 'personachat_newsetting': '', 'personachat_interact': False, \
               'personachat_pdmn': False, 'personachat_tfidfperp': False, 'personachat_learnreweight': False, \
               'personachat_embshareonly_pm_dec': False, 'personachat_s2sinit': False, 'interactive_mode': True, \
               'use_persona': 'self', 'parlai_home': '/home/christoph/Documents/Roboy/ParlAI', 'override': {}, \
               'starttime': 'Jun15_16-58'}
        opt['model_type'] = 'profilememory'  # for builder
        opt['task'] = 'parlai.agents.local_human.local_human:LocalHumanAgent'

        # Create model and assign it to the specified task
        agent = create_agent(opt, requireModelExists=True)
        world = create_task(opt, agent)
        #### model ready to go ####

        logging.info("Service /roboy/cognition/generative_nlp/answer is ready")

        # wait for the service request, generate the answer, and send it back
        while True:
            try:
                request = await websocket.recv()

                sentence = json.loads(request)["args"]["text_input"]
                print(sentence)
                answer = world.parley(sentence)
                model_response = answer
                print(model_response)
                srv_response = {}
                answer = {}

                if isinstance(model_response, list):
                    text = model_response[0]['dec_inp']
                else:
                    text = model_response

                answer["text_output"] = ''.join([i if ord(i) < 128 else '' for i in text])  # strip down unicode

                srv_response["values"] = answer
                srv_response["op"] = "service_response"
                srv_response["id"] = "service_request:/roboy/cognition/generative_nlp/answer:" + str(i)
                srv_response["result"] = True
                srv_response["service"] = "/roboy/cognition/generative_nlp/answer"
                i += 1

                await websocket.send(json.dumps(srv_response))

            except Exception as e:
                logging.exception("Oopsie! Got an exception in generative_nlp")


logging.basicConfig(level=logging.INFO)
asyncio.get_event_loop().run_until_complete(service_callback())
