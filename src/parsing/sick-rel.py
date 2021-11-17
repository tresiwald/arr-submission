import glob

import pandas

from parsing.parsing_util import save_topic_folds

data_path = "../../data/"
task = "sick-nli"

samples = pandas.read_csv("../../data/SICK.txt", delimiter="\t")[["pair_ID",	"sentence_A",	"sentence_B",	"relatedness_score", "SemEval_set"]]

samples.columns = ["id", "sentence1", "sentence2", "label", "set"]

set_mapping = {
    "TRAIN": "train",
    "TRIAL": "dev",
    "TEST": "test",
}



samples["set"] = samples["set"].apply(lambda set: set_mapping[set])
samples["label"] = samples["label"].apply(lambda label: label)
samples.to_csv(data_path + task + ".csv", index=False)