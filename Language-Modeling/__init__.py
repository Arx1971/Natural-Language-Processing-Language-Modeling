import re
import string


# data pre-processing

def load_data_set(filename):
    with open(filename, "r") as lines:
        str_array = []
        for line in lines:
            line = line[0:len(line) - 1]
            str_array.append("<s> " + line.lower() + " </s>\n")

    return str_array


def training_data_process(data_set, filename):
    file = open("updated-" + filename, "w")
    dictionary = dict()
    token_counter = 0
    for sentence in data_set:
        words = sentence.split()
        for word in words:
            token_counter += 1
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1

    dictionary["<unk>"] = 1

    for sentence in data_set:
        words = sentence.split()
        for word in words:
            if dictionary[word] == 1:
                file.write(" <unk>")
                del dictionary[word]
                dictionary["<unk>"] += 1
            else:
                file.write(" " + word)
        file.write("\n")

    file.close()

    print("Total Number of Unique Words in Training Corpus: ", len(dictionary))
    print("Total Number of Token in Training Corpus: ", token_counter)

    return dictionary


def test_data_process(dictionary, dataset, filename):
    file = open("updated-" + filename, "w")
    for sentence in dataset:
        words = sentence.split()
        for word in words:
            if word in dictionary:
                file.write(" " + word)
            else:
                file.write(" " + "<unk>")
        file.write("\n")
    file.close()


def percentage_word_and_token(test_data, train_data):
    train_data_map = dict()
    test_data_map = dict()
    test_token_counter = 0
    train_token_counter = 0

    for sentence in train_data:
        words = sentence.split()
        for word in words:
            train_token_counter += 1
            if word not in train_data_map:
                train_data_map[word] = 1
            else:
                train_data_map[word] += 1

    for sentence in test_data:
        words = sentence.split()
        for word in words:
            test_token_counter += 1
            if word not in test_data_map:
                test_data_map[word] = 1
            else:
                test_data_map[word] += 1

    print(len(train_data_map), " ", train_token_counter)
    print(len(test_data_map), " ", test_token_counter)


training_data_set = load_data_set("brown-train.txt")
test_data_set = load_data_set("brown-test.txt")
dictionary = training_data_process(training_data_set, "brown-train.txt")
test_data_process(dictionary, test_data_set, "brown-test.txt")

percentage_word_and_token(test_data_set, training_data_set)
