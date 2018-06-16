# Training

## Background ParlAI Training
There are many many options and arguments, your best source to get an overview is the shell script ./roboy_train_profilememory.sh in ss18_showmaster/DeepQA/parlai or the according ParlAI functions
### Training Options
- define a timeframe in which to train
- define a number of epochs to train
- PATIENCE: when the validation accuracy doesn't improve X times in a row training is considered finished
### Pre-trained models & fine-tuning
- There are pre-trained models available through model zoo. get them for instance through running python projects/convai2/baselines/profilememory/interactive.py from the ParlAI folder
- copy profilememory_convai2_model to /tmp/, this is where models will end up
- when calling the training, include --dict-file models:convai2/profilememory/profilememory_convai2.dict in the call. This will make the training script load profilememory_convai2_model from /tmp/ (see [ParlAI Github Issue 823](https://github.com/facebookresearch/ParlAI/issues/823))

## How To: Set up training
- go to shell script in ss18_showmaster/DeepQA_ParlAI/train
- set your hyper parameters
- if batches are too large you will run into CUDA memory errors (-bs 32 works)
- model trains very slow (training and validation accuracy ~0 for very long). Set validation metric to f1 to not have unintended stopping due to patience
- push to git

## How To: Train
- [Boot useastdeepqa VM instance on GCP](https://console.cloud.google.com/compute/ )
- Click SSH to open new shell in browser (alternatively, install gcloud command line tools on local machine)
- update ss18_showmaster git
- do: $ screen
- activate virtual environment ~/venvParlAI36/bin/activate
- run shell script ./roboy_train_profilememory.sh from ss18_showmaster/DeepQA_ParlAI/train
- log-file will be saved to path in shell script
- model will be saved to /tmp/
- Press Ctrl+a, Ctrl+d in quick sequence
- screen is now detached
- now you can close the shell while training continues
- to return to this screen, open shell and do screen -r (or screen -ls if multiple; don't forget to detach again)
- You can close the shell now (or just keep pressing Ctrl+a, Ctrl+d until all shells are closed)

## How To: Retrieve Data and Evaluate Training
- do gcloud compute scp --recurse team_roboy@ubuntu1604uswest1b:~/ParlAI/data/models/convai2/profilememory ~/Desktop to retrieve log files
- locally, activate your virtual environment and start the iPython AnalysisNotebook and follow the process there
- you might need to adapt names/directories
- you might need to adapt the end criteria under 4 to match your log file
- do gcloud compute scp --recurse team_roboy@ubuntu1604uswest1b:/tmp/ ~/Desktop to retrieve model if log files show it is valuable
- ... to interactively test them
- shut down the computing engine after training, otherwise Roboy will still be charged. (currently ~$1.50/h)

# About GCloud Compute Engine
## Set up
- get [gcloud command line tools](https://cloud.google.com/sdk)
- put the folder somewhere where you wont delete it
- install using ./google-cloud-sdk/install.sh
- [Quickstart](https://cloud.google.com/sdk/docs/quickstart-macos)
- new terminal window
- https://cloud.google.com/compute/docs/gcloud-compute/
./google-cloud-sdk/bin/gcloud init

## File Transfer
- Copy files from Instance to local machine: gcloud compute copy-files [INSTANCE_NAME]:[REMOTE_FILE_PATH] [LOCAL_FILE_PATH]
- i.e. in a terminal do 'gcloud compute scp --recurse team_roboy@ubuntu1604uswest1b:~/ParlAI/data/models/convai2/profilememory ~/Desktop'
- [Further file transfer help](https://cloud.google.com/compute/docs/instances/transfer-files)

## Configuration (21.05.2018)

### Structure:
- Showmaster git
- ParlAI git
- Pytorch venv
- (Lua Torch venv)

### GCP
- us-west1-b
- 8 vCPU
- 52 GB memory (personachat data set needs >32GB RAM to work with torch)
- 1 NVIDIA Tesla K80 (usable in us-west1-b)
- Ubuntu 16.04 LTS
- 50GB persistent storage 
- if you require more [storage](https://cloud.google.com/compute/docs/disks/add-persistent-disk)
- if you change these settings make sure you crosscheck if you need a [quota increase](https://console.cloud.google.com/iam-admin/quotas) (especially for GPU!!) 

### Software
- Python 3.6
- [Nvidia drivers](https://cloud.google.com/compute/docs/gpus/add-gpus)
- Cuda 9.0 (9.1 does not work yet (trust me I tried))
- [Torch Lua 5.2](http://torch.ch/docs/getting-started.html) ([mind issues!](https://github.com/torch/distro/issues/239))
- [Screen reconnection](https://www.howtogeek.com/howto/ubuntu/keep-your-ssh-session-running-when-you-disconnect/)

#### Further Requirements (through pip3, these are just all you need, not all on the GCP but also locally for ROS, Analysis etc..)
- [Spacy](https://spacy.io/usage/) (make sure to get module en) 
- torchtext
- stop-words
