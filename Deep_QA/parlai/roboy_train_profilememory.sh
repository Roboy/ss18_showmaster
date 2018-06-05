#!/bin/bash
# clear
#screen -S roboy

python3 train_roboy.py -hs 1024 -emb 300 -nl 2 -lr 0.01 -dr 0.2 -tr 100 -dec same -opt adam -ltim 10 -vtim 600 -vme 1000 -vp 10 -vmt accuracy -vmm max -vcut 1.0 -dbf True -lfc False >& ../../../ParlAI/data/models/convai2/profilememory/_profilememory_log.txt

# 2>&1 | tee ../../../ParlAI/data/models/convai2/profilememory/_profilememory_log.txt

# Logging
#

