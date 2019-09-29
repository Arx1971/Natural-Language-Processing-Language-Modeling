def load_data_set(filename):
    with open(filename, "r") as lines:
        str_array = []
        for line in lines:
            str_array.append(line)

    return str_array


def unique_word_type_bigram(dataset):
    dictionary = dict()
    total_token = 0
    for sentence in dataset:
        words = sentence.split()
        for i in range(0, len(words) - 1):
            word = (words[i], words[i + 1])
            total_token += 1
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    return dictionary, total_token



def percentage_bigrams(dictionary, dataset):
    test_dictionary_match = dict()
    test_dictionary_non_match = dict()
    total_number_token_match = 0
    total_number_token_non_match = 0
    for sentence in dataset:
        words = sentence.split()
        for i in range(0, len(words) - 1):
            word = (words[i], words[i + 1])
            if word in dictionary:
                total_number_token_match += 1
                if word in test_dictionary_match:
                    test_dictionary_match[word] += 1
                else:
                    test_dictionary_match[word] = 1
            else:
                total_number_token_non_match += 1
                if word in test_dictionary_non_match:
                    test_dictionary_non_match[word] += 1
                else:
                    test_dictionary_non_match[word] = 1
    print(len(test_dictionary_non_match), " ", total_number_token_non_match)


train_data_set = load_data_set("updated-brown-train.txt")
brown_data_set = load_data_set("updated-brown-test.txt")

bigrams_dictionary = unique_word_type_bigram(train_data_set)

print(len(bigrams_dictionary[0]), bigrams_dictionary[1])
percentage_bigrams(bigrams_dictionary, brown_data_set)
