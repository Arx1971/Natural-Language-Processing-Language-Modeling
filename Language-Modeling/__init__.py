import string
import re


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


def duplicates_word_to_unk(data_set):
    dictionary = {}
    for sentence in data_set:
        words = sentence.split()
        for word in words:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1

    return dictionary


# main method


path = "/home/adnanrahin/source-code/PycharmProjects/Natural-Language-Processing-Language-Modeling"

brown_test_path = path + "/Data-Set/brown-test.txt"
brown_train_path = path + "/Data-Set/brown-train.txt"

brown_test_data = padding_model(brown_test_path)
brown_train_data = padding_model(brown_train_path)

brown_test_data = lower_case_all_words(brown_test_data)
brown_train_data = lower_case_all_words(brown_train_data)

dictionary = duplicates_word_to_unk(brown_train_data)

for word, count in dictionary.items():
    print(word, count)
