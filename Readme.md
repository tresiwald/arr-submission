# Readme
With this repository we make the source code of our approach of **Exploiting Dataset Structures to Improve Pairwise Sentence Classification** public available. It includes the folder `src` with the code, `data` that includes an toy dataset example, and `experiments` that includes additional details of the experiments in the paper.
These details include:
* The optimized batch sizes for the three experiments `batch-sizes_experiment-i.csv, batch-sizes_experiment-ii.csv, batch-sizes_experiment-iii.csv`
* The results of the instability test using the Brown-Forsyth test `stability_experiment-i.csv, stability_experiment-ii.csv, stability_experiment-iii.csv`

## Build Docker
For setting up the docker run the following command:
```
docker-compose build
docker-compose up lab
```
After building the docker container and start it you can access a JupyterLab instance on port `8080.

## Prepare Datasets
To prepare all the dataset for using with our approach you find in `src/parsing` the python code to parse all the used dataset und generate the different folds. For this purpose please put the downloaded dataset in the folder `data`.

If you whish to prepare an own dataset, please arange it as csv with the columns id, sentence1, sentence2, label, and set. You will find an toy example in the `data` folder with 13 sentence pairs for five topics arranged in three folds.

## Usage

You can use our different batching strategies with the python script `run.py`. For gathering the performance please create an wandb.ai account and login with the following bash command `wandb login`. 

To start a training you can call the script `python3 run.py` and provide the following parameters:
* `--data_file`, the path to the specific file with the training instances, default `../data/sample_fold_0.csv`
* `--num_labels`, the number of labels of the training task, default `2
* `--directed`, a flag parameter that indicate that the label describes a directed, if not just leave it out
* `--dev_sets`, the sets using for development in the provided csv file, default `dev`
* `--test_sets`, the sets using for testing in the provided csv file, default `dev`
* `--model_name`, the Hugginface tag of the pre-trained language model you wish to use, default `bert-base-uncased`
* `--strategy`, the specific batching strategy you want to apply either `BI_BASELINE, BI_NODE, BI_EDGE1, BI_EDGE2` for bi-enocders or `CROSS_BASELINE, CROSS_NODE, CROSS_EDGE1, CROSS_EDGE2` for cross-encoders, default `BI_NODE`
* `--seed`, the random seed to use, default `0`
* `--batch_size`, the number of nodes or edges to sample within one batch, default `8`
* `--learning_rate`, the learning rate to use, default `0.00002`
* `--num_epochs`, the number of epochs to train on, default `5`
* `--warmup_proportion`, portion of epochs to use as warmup period, default `0.1
* `--wandb_tag_prefix`, the prefix for the wandb tag, default `8`
* `--wandb_project`, the wandb project to use, default ``
* `--max_tokens`, the maximum of tokens to process within one step. If batch has more token, the training use gradient accumulation to efficient process a batch, default `6000`
* `--strategy_baseline_accumulation_steps`, the number of gradient accumulation steps to apply for the training the baseline model for example with 2 a batch with 8 instance is divided into two batch of 4 instances, default `2`
