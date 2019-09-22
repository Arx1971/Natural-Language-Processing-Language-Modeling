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
    pattern = "[A-Za-z]"
    openfile = open("new-brown-train-data.txt", "w")
    for sentence in data_set:
        words = sentence.split()
        openfile.write("<s>")
        for word in words[1:len(words) - 1]:
            if re.match(pattern, word):
                if word not in dictionary:
                    dictionary[word] = 1
                    openfile.write(" " + word)
                else:
                    dictionary[word] += 1
                    openfile.write(" " + "<unk>")
            else:
                openfile.write(" " + word)
        openfile.write(" </s>\n")

    openfile.close()
    return dictionary


def test_data_not_in_train_data(dictionary, data_set):
    openfile = open("new-brown-test-data.txt", "w")
    pattern = "[A-Za-z]"
    for sentence in data_set:
        words = sentence.split()
        openfile.write("<s>")
        for word in words[1:len(words) - 1]:
            if re.match(pattern, word):
                if word not in dictionary:
                    openfile.write(" " + "<unk>")
                else:
                    openfile.write(" " + word)
            else:
                openfile.write(" " + word)
        openfile.write(" </s>\n")

    openfile.close()


brown_test_path = "brown-test.txt"
brown_train_path = "brown-train.txt"

brown_test_data = padding_model(brown_test_path)
brown_train_data = padding_model(brown_train_path)

brown_test_data = lower_case_all_words(brown_test_data)
brown_train_data = lower_case_all_words(brown_train_data)

dictionary = duplicates_word_to_unk(brown_train_data)

test_data_not_in_train_data(dictionary, brown_test_data)

counter = 0
