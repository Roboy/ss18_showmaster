# /bin/bash
export PYTHONPATH=
export PATH=~/anaconda3/bin:$PATH

source activate python35

python gnlp_ros_srv.py --modelTag pretrainedv2 --test ros



## get this to point to venv for ParlAI
# source activate python36

#python3 projects/convai2/baselines/profilememory/interactive.py