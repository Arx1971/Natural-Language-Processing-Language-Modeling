import re
import string


# data pre-processing

def load_data_set(filename):
    with open(filename, "r") as lines:
        str_array = []
        for line in lines:
            line = line[0:len(line) - 1]
            str_array.append("<s> "+ line.lower() + " </s>\n")

    return str_array


def data_process(data_set, filename):
    file = open("updated-" + filename, "w")
    dictionary = dict()
    pattern = "[A-Za-z]"
    for sentence in data_set:
        words = sentence.split()
        for word in words:
            if re.match(pattern, word):
                if word not in dictionary:
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1

    for sentence in data_set:
        words = sentence.split()
        for word in words:
            if re.match(pattern, word):
                if dictionary[word] == 1:
                    file.write(" <unk>")
                else:
                    file.write(" " + word)
            else:
                file.write(" " + word)
        file.write("\n")
    file.close()


training_data_set = load_data_set("brown-train.txt")
data_process(training_data_set, "brown-train.txt")