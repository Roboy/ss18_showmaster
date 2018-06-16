## Quick Start

- start the useastdeepqa VM instance on the [Google Cloud Console](https://console.cloud.google.com/compute/ )
- Click SSH to open new shell in browser (alternatively, install gcloud command line tools on local machine)
- activate virtual environment (depending on what you want to do)
- Pytorch: source ~/venvParlAI36/bin/activate
- Lua torch: source ~/luatorch_venv/bin/activate (outdated as we do not use this!)
- go to Git repo cd ss18_showmaster/
- shut down the computing engine after training, otherwise Roboy will still be charged. (currently ~$0.50/h)

## Set up
- get [gcloud command line tools](https://cloud.google.com/sdk)
put the folder somewhere where you wont delete it
install using ./google-cloud-sdk/install.sh
[Quickstart](https://cloud.google.com/sdk/docs/quickstart-macos)
new terminal window
https://cloud.google.com/compute/docs/gcloud-compute/
./google-cloud-sdk/bin/gcloud init

## File Transfer
gcloud compute scp --recurse team_roboy@ubuntu1604uswest1b:~/ParlAI/data/models/convai2/profilememory ~/Desktop
printed bold: just copy path from shell.
https://cloud.google.com/compute/docs/instances/transfer-files
Copy files from Instance to local machine: gcloud compute copy-files [INSTANCE_NAME]:[REMOTE_FILE_PATH] [LOCAL_FILE_PATH]


## Configuration (21.05.2018)

### Structure:
- Boot Disk (50GB)
- Pytorch venv
- Lua Torch venv
- Showmaster git
- ParlAI git

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
- [Torch Lua 5.2](http://torch.ch/docs/getting-started.html) ([mind issues](https://github.com/torch/distro/issues/239 !!))
- [Screen reconnection](https://www.howtogeek.com/howto/ubuntu/keep-your-ssh-session-running-when-you-disconnect/)

#### Further Requirements (through pip3, these are just all you need, not all on the GCP but also locally for ROS, Analysis etc..)
- [Spacy](https://spacy.io/usage/) (make sure to get module en) 
- torchtext (for personachat projects)
- stop-words
- jupyter
- matplotlib
- tee
- websockets
