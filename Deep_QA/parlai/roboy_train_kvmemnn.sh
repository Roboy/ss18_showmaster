#!/bin/bash

clear

#screen -S roboy

python3 ../../../ParlAI/projects/convai2/baselines/kvmemnn/train.py \
######################## arguments from scripts/train_model.py: ########################
# evaltask
#-et\
# display examples:
--display-examples False\
# train n epochs (std -1):
-eps -1\
# max train time: (std 28800)
-ttim 28800\
# log every n seconds (std 10):
-ltim 2\
# validate every n seconds: (std 900)
-vtim 150\
## save every n seconds:
-stim -1\
# save after validation:
-sval False\
# max examples to use during validation (-1 uses all, std 100000):
-vme 10000\
# validation patience -> training over after not achieving better validation n times (std -1):
-vp 10\
# validation metric (std accuracy):
-vmt accuracy\
# validation metric mode (std max):
-vmm max\
# validation-cutoff
-vcut 1.0\
# dict-build-first
-dbf True\
# load-from-checkpoint
-lfc False\
######################## arguments from projects/personachat/kvmemnn.py ########################
--hops 1\
--twohop_range 100\
#num lins projecting after hops
--lins 0\
# embedding size
-esz 128\
# max norm of word embeddings
-enorm 10\
# whether LHS and RHS share embeddings
-shareEmb True,
#learning rate
-lr 0.005\
# margin
-margin 0.3\
# loss choices={'cosine', 'nll'})
-loss cosine\
# Optimizer
-opt sgd\
# truncate to speed up training (may reduce accuracy) -1 gives all in/out minimum length
-tr -1\
# number k of negative samples per example
-k 10\
# include query as a negative
--parrot-neg 0\
# take next utt
--take-next-utt False\
# Use frequency based normalization for embeddings
--tfidf False\
# size of negative sample cache to draw from
-cs 1000\
# Number of past tokens to remember
-hist 100\
# Keep replies in the history, or not
-histr label\
# interactive mode
--interactive-mode False\
######################## arguments from memnn.py ########################
#--init-model None\
#--embedding-size 128\
#--hops 3\
#--mem-size 100\
#--time-features True\
#--position-encoding False\
#--output rank\
#--rnn-layers 2\
#--dropout 0.1\
#--optimizer adam\
#--no-cuda False
#--gpu -1
#-histr
# learning rate (std 0.1):
#-lr 0.01\
######################## logging ########################
# logging
>& ../../../ParlAI/data/models/convai2/kvmemnn/kvmemnn_log.txt



#| tee data/models/convai2/profilememory/profilememory.log
# -esz 128

