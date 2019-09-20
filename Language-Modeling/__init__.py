import math
import re


# Pad each sentence
def padding_model(flie_path):
    with open(flie_path, "r") as lines:
        str_array = []
        for line in lines:
            line = line[0:len(line) - 1]
            str_array.append("<s> " + line + " </s>")

    return str_array


brown_test_path = "/home/adnanrahin/source-code/PycharmProjects/Natural-Language-Processing-Language-Modeling/Data-Set/brown-test.txt"
brown_train_path = "/home/adnanrahin/source-code/PycharmProjects/Natural-Language-Processing-Language-Modeling/Data-Set/brown-train.txt"

brown_test_data = padding_model(brown_test_path)
brown_train_data = padding_model(brown_train_path)

