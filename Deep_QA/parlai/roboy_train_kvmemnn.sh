#!/bin/bash

clear

#screen -S roboy

python3 ../../../ParlAI/projects/convai2/baselines/kvmemnn/train.py >& ../../../ParlAI/data/models/convai2/kvmemnn/kvmemnn.txt
#| tee data/models/convai2/profilememory/profilememory.log
# -esz 128
