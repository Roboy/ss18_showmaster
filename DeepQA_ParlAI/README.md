## Setup
### Requirements:
- Python 36
- ParlAI
- [PyTorch](http://pytorch.org/)
- ss18_showmaster

### Installing ParlAI

Run the following commands to clone the repository and install ParlAI:

```bash
git clone https://github.com/facebookresearch/ParlAI.git ~/ParlAI
cd ~/ParlAI; python setup.py develop
```

This will link the cloned directory to your site-packages.

This is the recommended installation procedure, as it provides ready access to the examples and allows you to modify anything you might need. This is especially useful if you if you want to submit another task to the repository.

All needed data will be downloaded to ~/ParlAI/data, and any non-data files (such as the MemNN code) if requested will be downloaded to ~/ParlAI/downloads. If you need to clear out the space used by these files, you can safely delete these directories and any files needed will be downloaded again.


## Examples


[ParlAI](https://github.com/facebookresearch/ParlAI/) (pronounced “par-lay”) is a framework for dialog AI research by Facebook, implemented in Python. See their website [http://parl.ai](http://parl.ai) for further docs

ParlAI is described in the following paper:
[“ParlAI: A Dialog Research Software Platform", arXiv:1705.06476](https://arxiv.org/abs/1705.06476).

For example, to see the training data, try:
```
python ~/ParlAI/examples/display_data.py -t convai2 -dt train
```

## Examples

You can run examples of training on this task in the `baselines` folder in this directory.

For example, you can download and interact with a pre-trained seq2seq model (based on ParlAI's implementation in parlai/agents/seq2seq) using `baselines/seq2seq/interact.py`, or train your own with the same parameters using the `train.py` file in that directory.

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

## Remarks on dataset versions

The several versions of the dataset can be accessed with `convai2:self`, `convai2:self_revised` and `convai2:none`.

These correspond to "original self persona", "revised self persona" and "no persona" in the original [PersonaChat](https://arxiv.org/pdf/1801.07243.pdf) paper.
However, in contrast to that dataset, we have modified the preprocessing and are generating a new hidden test set. We have also added training examples from the perspective of both speakers and additional candidates to support training / evaluating using a ranking loss.

You can use the `none` mode to contrast your model's ability to take advantage of its persona with `self`, but `self` is the default setting for the task, and you will be evaluate on 'self' and 'self_revised'.

You can see examples of models prepared for the original (non-competition) PersonaChat task [here](https://github.com/facebookresearch/ParlAI/tree/master/projects/personachat), which should generally transfer pretty easily to this task. However, we will continue to add baseline models to this project folder as we run experiments.


## ParlAI Support
ParlAI is currently maintained by Emily Dinan, Alexander H. Miller, Kurt Shuster, Jack Urbanek and Jason Weston, a very helpful team. If you have any questions, bug reports or feature requests, post on their [Github Issues page](https://github.com/facebookresearch/ParlAI/issues) and issues will usually be resolved within hours (NY time!).


