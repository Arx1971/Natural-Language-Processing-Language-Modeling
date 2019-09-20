import math
import re
import string
from string import punctuation


# Section 1.1 Pre-Processing the data set

# Pad each sentence
def padding_model(file_path):
    with open(file_path, "r") as lines:
        str_array = []
        for line in lines:
            line = line[0:len(line) - 1]
            str_array.append("<s> " + line + " </s>")

    return str_array


# LowerCase all words

def lower_case_all_words(data_set):
    for i in range(0, len(data_set)):
        data_set[i] = data_set[i].lower()

    return data_set


# Replace all words occurring in the training data once with the token <unk>

def replace_to_unk(data_set):
    duplicates = set()
    modified_data_set = []
    for i in range(0, len(data_set)):

        sentence = data_set[i].strip()

        words = sentence.split()

        table = str.maketrans('', '', string.punctuation)

        stripped = [words[j].translate(table) for j in range(1, len(words) - 1)]

        for j in range(0, len(stripped)):
            if stripped[j] in duplicates:
                stripped[j] = "<unk>"
            else:
                duplicates.add(stripped[j])
        stripped.insert(0, "<s>")
        stripped.append("</s>")
        modified_data_set.append(stripped)

    return modified_data_set


# main method

path = "/home/adnanrahin/source-code/PycharmProjects/Natural-Language-Processing-Language-Modeling"

brown_test_path = path + "/Data-Set/brown-test.txt"
brown_train_path = path + "/Data-Set/brown-train.txt"

brown_test_data = padding_model(brown_test_path)
brown_train_data = padding_model(brown_train_path)

brown_test_data = lower_case_all_words(brown_test_data)

brown_train_data = lower_case_all_words(brown_train_data)

new_data_set = replace_to_unk(brown_train_data)

for i in range(0, len(new_data_set)):
    print(new_data_set[i])
# v = "my name is megatron's."
#
# words = v.split()
#
# table = str.maketrans('', '', string.punctuation)
# stripped = [w.translate(table) for w in words]
# print(stripped)
