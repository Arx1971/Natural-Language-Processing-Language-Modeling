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


browntest = "/home/adnanrahin/source-code/PycharmProjects/Natural-Language-Processing-Language-Modeling/Data-Set/brown-test.txt"

str = padding_model(browntest)
for i in range(0, len(str)):
    print(str[i])
