## What you need:
- ParlAI
- ss18_showmaster
in same folder. 

## Requirements

ParlAI currently requires Python3.6.

Dependencies of the core modules are listed in requirement.txt.

Several models included (in parlai/agents) have additional requirements.
Profilememory requires installing [PyTorch](http://pytorch.org/). See the website for installation instructions.

## Installing ParlAI

Run the following commands to clone the repository and install ParlAI:

```bash
git clone https://github.com/facebookresearch/ParlAI.git ~/ParlAI
cd ~/ParlAI; python setup.py develop
```

This will link the cloned directory to your site-packages.

This is the recommended installation procedure, as it provides ready access to the examples and allows you to modify anything you might need. This is especially useful if you if you want to submit another task to the repository.

All needed data will be downloaded to ~/ParlAI/data, and any non-data files (such as the MemNN code) if requested will be downloaded to ~/ParlAI/downloads. If you need to clear out the space used by these files, you can safely delete these directories and any files needed will be downloaded again.

## Setup:
- Follow PArlAI instructions
- [PyTorch](http://pytorch.org/)

[ParlAI](https://github.com/facebookresearch/ParlAI/) (pronounced “par-lay”) is a framework for dialog AI research by Facebook, implemented in Python. See their website [http://parl.ai](http://parl.ai) for further docs

ParlAI is described in the following paper:
[“ParlAI: A Dialog Research Software Platform", arXiv:1705.06476](https://arxiv.org/abs/1705.06476).

Display 10 random examples from task 1 of the "1k training examples" bAbI task:
```bash
python examples/display_data.py -t babi:task1k:1
```

Displays 100 random examples from multi-tasking on the bAbI task and the SQuAD dataset at the same time:
```bash
python examples/display_data.py -t babi:task1k:1,squad -n 100
```

Evaluate on the bAbI test set with a human agent (using the local keyboard as input):
```bash
python examples/eval_model.py -m local_human -t babi:Task1k:1 -dt valid
```

Evaluate an IR baseline model on the validation set of the Movies Subreddit dataset:
```bash
python examples/eval_model.py -m ir_baseline -t "#moviedd-reddit" -dt valid
```

Display the predictions of that same IR baseline model:
```bash
python examples/display_model.py -m ir_baseline -t "#moviedd-reddit" -dt valid
```

Train a seq2seq model on the "10k training examples" bAbI task 1 with batch size of 32 examples until accuracy reaches 95% on validation (requires pytorch):
```bash
python examples/train_model.py -t babi:task10k:1 -m seq2seq -mf /tmp/model_s2s -bs 32 -vtim 30 -vcut 0.95
```

Trains an attentive LSTM model on the SQuAD dataset with a batch size of 32 examples (pytorch and regex):
```bash
python examples/train_model.py -m drqa -t squad -bs 32 -mf /tmp/model_drqa
```

Tests an existing attentive LSTM model (DrQA reader) on the SQuAD dataset from our model zoo:
```bash
python examples/eval_model.py -t squad -mf "models:drqa/squad/model"
```



## ParlAI Support
The PArlAI team is very helpful. ParlAI is currently maintained by Emily Dinan, Alexander H. Miller, Kurt Shuster, Jack Urbanek and Jason Weston. If you have any questions, bug reports or feature requests, post on their [Github Issues page](https://github.com/facebookresearch/ParlAI/issues) and issues will usually be resolved within hours (NY time!).


