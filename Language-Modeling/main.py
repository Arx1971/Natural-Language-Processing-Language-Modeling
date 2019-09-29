import re
import string


def load_data_set(filename):
    with open(filename, "r") as lines:
        str_array = []
        for line in lines:
            line = line.lower()
            line = line[0:len(line) - 1]
            str_array.append("<s> " + line + " </s>\n")

    return str_array


def data_Match(dictionary, data):
    match = dict()
    non_match = dict()

    for sentence in data:
        words = sentence.split()
        for word in words:
            word = word.lower()
            if word in dictionary:
                if word in match:
                    match[word] += 1
                else:
                    match[word] = 1
            elif word not in dictionary:
                if word in non_match:
                    non_match[word] += 1
                else:
                    non_match[word] = 1


def unique_word(data):
    dictionary = dict()
    for sentence in data:
        words = sentence.split()
        for word in words:
            # word = word.lower()
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1

    return dictionary


def printer(data):
    for sentence in data:
        print(sentence)


data = load_data_set("brown-train.txt")

dictionary = unique_word(data)
test_data = load_data_set("brown-test.txt")
printer(test_data)
