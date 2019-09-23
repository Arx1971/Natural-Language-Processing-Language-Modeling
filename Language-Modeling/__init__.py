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
                    del dictionary[word]
                else:
                    file.write(" " + word)
            else:
                file.write(" " + word)
        file.write("\n")

    file.close()

    return dictionary


def test_data_process(dictionary, dataset, filename):
    file = open("updated-" + filename, "w")
    pattern = "[A-Za-z]"
    for sentence in dataset:
        words = sentence.split()
        for word in words:
            if re.match(pattern, word):
                if word in dictionary:
                    file.write(" " + word)
                else:
                    file.write(" " + "<unk>")
            else:
                file.write(" " + word)
        file.write("\n")
    file.close()


def total_number_of_words_token(dictionary):
    total_word_count = 0
    for word, count in dictionary.items():
        total_word_count += count

    return total_word_count


training_data_set = load_data_set("brown-train.txt")
test_data_set = load_data_set("brown-test.txt")

dictionary = training_data_process(training_data_set, "brown-train.txt")
test_data_process(dictionary, test_data_set, "brown-test.txt")

print("Total Number of Unique Words in the Training Corpus: ", len(dictionary) + 3)
print(total_number_of_words_token(dictionary))
