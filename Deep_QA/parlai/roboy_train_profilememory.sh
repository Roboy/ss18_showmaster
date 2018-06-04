#!/bin/bash

clear

#screen -S roboy

python3 ../../../ParlAI/projects/convai2/baselines/profilememory/train.py -lr 0.1 -bs 32 >& ../../../ParlAI/data/models/convai2/profilememory/profilememory.txt
#| tee data/models/convai2/profilememory/profilememory.log
# -esz 128
