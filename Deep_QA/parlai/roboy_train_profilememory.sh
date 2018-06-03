#!/bin/bash

clear

#screen -S roboy

python3 ../../../ParlAI/projects/convai2/baselines/profilememory/train.py -hs 1024 -nl 3 -lr 0.001 -dr 0.2 -att general >& ../../../ParlAI/data/models/convai2/profilememory/profilememory.txt
#| tee data/models/convai2/profilememory/profilememory.log
# -esz 128
