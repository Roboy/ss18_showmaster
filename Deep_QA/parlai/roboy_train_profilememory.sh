#!/bin/bash

clear

#screen -S roboy

python3 ../../../ParlAI/projects/convai2/baselines/profilememory/train.py -hs 256 -nl 2 -lr 0.001 -dr 0.2 -att general -bs 32 >& ../../../ParlAI/data/models/convai2/profilememory/profilememory.txt
#| tee data/models/convai2/profilememory/profilememory.log
# -esz 128
