import re
import string


def load_data_set(filename):
    with open(filename, "r") as lines:
        str_array = []
        for line in lines:
            str_array.append(line)

    return str_array


def unique_word_in_train(data):
    dictionary = dict()

    for sentence in data:
        words = sentence.split()
        for word in words:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    print(len(dictionary))

    return dictionary


def method(dictionary, data):
    count = 0
    for sen in data:
        words = sen.split()
        for word in words:
            if word in dictionary:
                count += 1
    print(count)


train = load_data_set("brown-train.txt")
test = load_data_set("brown-test.txt")

dictionary = unique_word_in_train(train)

method(dictionary, test)
