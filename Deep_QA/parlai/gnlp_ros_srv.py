import os
import logging

import asyncio
import websockets
import json as json

import pdb

from chatbot import chatbot

async def service_callback():
    async with websockets.connect('ws://localhost:9090') as websocket:

        # advertise the service
        await websocket.send("{ \"op\": \"advertise_service\",\
                      \"type\": \"roboy_communication_cognition/GenerateAnswer\",\
                      \"service\": \"/roboy/cognition/generative_nlp/answer\"\
                    }")

        i = 1 # counter for the service request IDs
        cb = chatbot.Chatbot()
        cb.main()


        logging.info("Service /roboy/cognition/generative_nlp/answer is ready")

            # wait for the service request, generate the answer, and send it back
        while True:
            try:
                request = await websocket.recv()

                sentence = json.loads(request)["args"]["text_input"]
                print(sentence)
                answer = cb.singlePredict(sentence,[])
                model_response = cb.textData.sequence2str(answer,clean=True)
                print(model_response)
                # '{x[0]}{0}\n{x[1]}{1}\n\n'.format(sentence, cb.textData.sequence2str(answer, clean=True), x=cb.SENTENCES_PREFIX)
                    
                # pdb.set_trace()
                # model_response = get_predicted_sentence(args, sentence, vocab, rev_vocab, model, sess)

                srv_response = {}
                answer = {}

                if isinstance(model_response, list):
                    text = model_response[0]['dec_inp']
                else:
                    text = model_response

                answer["text_output"] = ''.join([i if ord(i) < 128 else '' for i in text]) # strip down unicode 

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