import re
import string


def load_data_set(filename):
    with open(filename, "r") as lines:
        str_array = []
        for line in lines:
            str_array.append(line)

    return str_array


def padding_sentence(filename):
    with open(filename, "r") as lines:
        str_array = []
        for line in lines:
            line = line[0:len(line) - 1]
            str_array.append("<s> " + line + " </s>")

    return str_array


def training_data_writer(data_set, filename):
    file = open("updated-" + filename, "w")
    dictionary = dict()
    token_counter = 0
    for sentence in data_set:
        words = sentence.split()
        for word in words:
            word = word.lower()
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1

    dictionary["<unk>"] = 0
    dictionary["<s>"] = 0
    dictionary["</s>"] = 0

    for sentence in data_set:
        words = sentence.split()
        file.write("<s>")
        dictionary["<s>"] += 1
        token_counter += 1
        for word in words:
            word = word.lower()
            token_counter += 1
            if dictionary[word] == 1:
                file.write(" <unk>")
                del dictionary[word]
                dictionary["<unk>"] += 1
            else:
                file.write(" " + word)
        file.write(" </s>\n")
        dictionary["</s>"] += 1
        token_counter += 1
    file.close()
    return dictionary


def test_data_writer(dictionary, dataset, filename):
    token_counter = 0
    test_dictionary = dict()
    test_dictionary["<unk>"] = 0
    test_dictionary["<s>"] = 0
    test_dictionary["</s>"] = 0
    file = open("updated-" + filename, "w")
    for sentence in dataset:
        words = sentence.split()
        file.write("<s>")
        test_dictionary["<s>"] += 1
        token_counter += 1
        for word in words:
            token_counter += 1
            word = word.lower()
            if word in dictionary:
                if word in test_dictionary:
                    test_dictionary[word] += 1
                else:
                    test_dictionary[word] = 1
                file.write(" " + word)
            else:
                file.write(" " + "<unk>")
                test_dictionary["<unk>"] += 1
        file.write(" </s>\n")
        test_dictionary["</s>"] += 1
        token_counter += 1
    file.close()

    return test_dictionary, token_counter


def unique_word_token_in_data(data_set):
    token_counter = 0
    train_dictionary = dict()

    for sentence in data_set:
        words = sentence.split()
        for word in words:
            word = word.lower()
            token_counter += 1
            if word not in train_dictionary:
                train_dictionary[word] = 1
            else:
                train_dictionary[word] += 1

    return train_dictionary, token_counter


def uingram_model(train_dictionary, test_dataset):
    token_counter_match = 0
    test_data_unique_word = dict()
    non_match_data = dict()
    total_token = 0
    for sentence in test_dataset:
        words = sentence.split()
        for word in words:
            word = word.lower()
            total_token += 1
            if word in train_dictionary:
                token_counter_match += 1
                if word in test_data_unique_word:
                    test_data_unique_word[word] += 1
                else:
                    test_data_unique_word[word] = 1
            else:
                if word not in non_match_data:
                    non_match_data[word] = 1
                else:
                    non_match_data[word] += 1

    word_type = len(non_match_data) / (len(test_data_unique_word) + len(non_match_data))
    word_token = (total_token - token_counter_match) / total_token
    print("Percentage of word token did not occur in the training: ", word_token * 100, "%")
    print("Percentage of word types did not occur in the training: ", word_type * 100, "%")

    return test_data_unique_word, non_match_data, token_counter_match


# Data Pre-Processing
training_data_set = load_data_set("brown-train.txt")
test_data_set = load_data_set("brown-test.txt")
learner_data_set = load_data_set("learner-test.txt")

dictionary = training_data_writer(training_data_set, "brown-train.txt")
processed_train_data = load_data_set("updated-brown-train.txt")

# problem 1:
arr_for_modified_train = unique_word_token_in_data(processed_train_data)
print("Total Number of Unique Word in Train-Data: ", len(arr_for_modified_train[0]))
print("Total Number of Token In Train-Data: ", arr_for_modified_train[1])

# Test Data Set Parse:
arr = unique_word_token_in_data(padding_sentence("brown-train.txt"))
print("BROWN-TEST-DATA: ")
arr_test_brown = uingram_model(arr[0], padding_sentence("brown-test.txt"))
print("LEARNER-TEST-DATA: ")
arr_test_learner = uingram_model(arr[0], padding_sentence("learner-test.txt"))

# update test file
test_updated_data = test_data_writer(dictionary, test_data_set, "brown-test.txt")
learner_updated_data = test_data_writer(dictionary, learner_data_set, "learner-test.txt")
learner_load = load_data_set("updated-learner-test.txt")
test_loader = load_data_set("updated-brown-test.txt")
arr = unique_word_token_in_data(learner_load)
brr = unique_word_token_in_data(test_loader)
print(len(arr[0]), " ", arr[1])
print(len(brr[0]), " ", brr[1])

print(dictionary['he']/498474)


