import re
import string


def load_data_set(filename):
    with open(filename, "r") as lines:
        str_array = []
        for line in lines:
            str_array.append(line)

    return str_array


def padding_sentence(data):
    file = open("updated-demo-data", "w")

    for sentence in data:
        words = sentence.split()
        file.write("<s>")
        for word in words:
            word = word.lower()
            file.write(" " + word)
        file.write(" </s>" + '\n')


def unique_word(data):
    dictionary = dict()
    for sentence in data:
        words = sentence.split()
        for word in words:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1

    for word, frequency in dictionary.items():
        print(word, frequency)


data = load_data_set("demo-data.txt")
unique_word(data)
padding_sentence(data)
