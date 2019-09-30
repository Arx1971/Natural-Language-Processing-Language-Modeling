import math


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


def unique_word_token_for_unigram(data_set):
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


def uingrams_model(train_dictionary, test_dataset):
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


# bigram processing

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


def bigrams_model(dictionary, dataset):
    test_dictionary_match = dict()
    test_dictionary_non_match = dict()
    total_number_token_match = 0
    total_number_token = 0
    for sentence in dataset:
        words = sentence.split()
        for i in range(0, len(words) - 1):
            word = (words[i], words[i + 1])
            total_number_token += 1
            if word in dictionary:
                total_number_token_match += 1
                if word in test_dictionary_match:
                    test_dictionary_match[word] += 1
                else:
                    test_dictionary_match[word] = 1
            else:
                if word in test_dictionary_non_match:
                    test_dictionary_non_match[word] += 1
                else:
                    test_dictionary_non_match[word] = 1
    word_type = len(test_dictionary_non_match) / (len(test_dictionary_non_match) + len(test_dictionary_match))
    word_token = (total_number_token - total_number_token_match) / total_number_token

    print("Percentage of word token did not occur in the training: ", word_token * 100, "%")
    print("Percentage of word types did not occur in the training: ", word_type * 100, "%")


def sentence_processing(sentence, dictionary):
    words = sentence.split()
    new_sentence = "<s> "
    for word in words:
        word = word.lower()
        if word in dictionary:
            new_sentence += word + " "
        else:
            new_sentence += "<unk> "
    new_sentence += "</s>"

    return new_sentence


def unigram_maximum_likelihood(dictionary, total_size, sentence):
    words = sentence.split()
    prob = 1.0
    for word in words:
        if word in dictionary:
            prob *= dictionary[word] / total_size
        elif word not in dictionary:
            return 0
    return prob


def log_probabilities_unigram(unigram_dictionary, sentence, v_size):
    log_prob = unigram_maximum_likelihood(unigram_dictionary, v_size, sentence)
    if log_prob is 0:
        return "0.0"
    else:
        return math.log(log_prob, 2)


def bigram_maximum_likelihood(bigram_dictionary, unigram_dictionary, sentence):
    words = sentence.split()
    prob = 1.0
    for i in range(0, len(words) - 1):
        var = (words[i], words[i + 1])
        key = bigram_dictionary.get(var, 0)
        if key is 0:
            return 0
        else:
            p = bigram_dictionary[var] / unigram_dictionary[words[i]]
            prob *= p
    return prob


def log_probabilities_bigram(bigram_dictionary, unigram_dictionary, sentence):
    log_prob = bigram_maximum_likelihood(bigram_dictionary, unigram_dictionary, sentence)
    if log_prob is 0:
        return "0.0"
    else:
        return math.log(log_prob, 2)


def bigram_add_smoothing(unigrams_dictionary, bigrams_dictionary, sentence, V):
    words = sentence.split()
    prob = 1.0
    for i in range(0, len(words) - 1):
        var = (words[i], words[i + 1])
        var2 = bigrams_dictionary.get(var, 0) + 1
        var3 = unigrams_dictionary.get(words[i], 0) + V
        prob *= (var2 / var3)

    return math.log(prob, 2)


def unigram_perplexity(unigram_dictionary, sentence, size):
    words = sentence.split()
    prob = 0.0
    for word in words:
        if word in unigram_dictionary:
            value = unigram_dictionary[word]
            p = value / size
            prob += math.log(p, 2)
        elif word not in unigram_dictionary:
            return "undefined"
    ans = math.pow(2, -(prob / len(words)))

    return ans, prob


def bigram_perplexity(unigram_dictionary, bigram_dictionary, sentence):
    words = sentence.split()
    prob = 0.0
    for i in range(0, len(words) - 1):
        var = (words[i], words[i + 1])
        if var in bigram_dictionary:
            p = bigram_dictionary[var] / unigram_dictionary[words[i]]
            prob += math.log(p, 2)  # check p is zero or not
        elif var not in bigram_dictionary:
            return "undefined"
    ans = math.pow(2, -(prob / len(words)))

    return ans


def bigram_add_one_smoothing_perplexity(unigrams_dictionary, bigrams_dictionary, sentence, V):
    words = sentence.split()
    prob = 0.0
    for i in range(0, len(words) - 1):
        var = (words[i], words[i + 1])
        var2 = bigrams_dictionary.get(var, 0) + 1
        var3 = unigrams_dictionary.get(words[i], 0) + V
        p = (var2 / var3)
        prob += math.log(p, 2)
    prob = prob / len(words)
    ans = math.pow(2, -prob)
    return ans


def unigram_perplexity_test_data(unigram_dictionary, test_data_set, unigram_total_token, total_token_in_test):
    prob_total = 0.0
    for sentence in test_data_set:
        prob = unigram_perplexity(unigram_dictionary, sentence, unigram_total_token)
        if prob is "undefined":
            return "undefined"
        else:
            prob_total += prob[1]
    ans = math.pow(2, -(prob_total / total_token_in_test))

    return ans


# Data Pre-Processing
training_data_set = load_data_set("brown-train.txt")
test_data_set = load_data_set("brown-test.txt")
learner_data_set = load_data_set("learner-test.txt")

dictionary = training_data_writer(training_data_set, "brown-train.txt")
processed_train_data = load_data_set("updated-brown-train.txt")

# problem 1:
arr_for_modified_train = unique_word_token_for_unigram(processed_train_data)
print("Total Number of Unique Word in Train-Data: ", len(arr_for_modified_train[0]))
print("Total Number of Token In Train-Data: ", arr_for_modified_train[1])

# Test Data Set Parse:
print("UNIGRAMS MODEL: ")
train_unigram = unique_word_token_for_unigram(padding_sentence("brown-train.txt"))
print("BROWN-TEST-DATA: ")
arr_test_brown = uingrams_model(train_unigram[0], padding_sentence("brown-test.txt"))
print("LEARNER-TEST-DATA: ")
arr_test_learner = uingrams_model(train_unigram[0], padding_sentence("learner-test.txt"))

# update test file
print("BIGRAMS MODEL: ")
test_updated_data = test_data_writer(dictionary, test_data_set, "brown-test.txt")
learner_updated_data = test_data_writer(dictionary, learner_data_set, "learner-test.txt")

learner_test_loader = load_data_set("updated-learner-test.txt")
brown_test_loader = load_data_set("updated-brown-test.txt")

train_bigrams = unique_word_type_bigram(processed_train_data)
print("BROWN-TEST-DATA: ")
bigrams_model(train_bigrams[0], brown_test_loader)
print("LEARNER-TEST-DATA: ")
bigrams_model(train_bigrams[0], learner_test_loader)

# Log probabilities for each model
# Log probabilities for Unigram

unigram_dictionary = arr_for_modified_train[0]
unigram_total_token = arr_for_modified_train[1]
bigram_dictionary = train_bigrams[0]
bigram_total_toke = train_bigrams[1]

print("Unigram Log probabilities for Each sentence: ")
sentence1 = sentence_processing("He was laughed off the screen .", arr_for_modified_train[0])
sentence2 = sentence_processing("There was no compulsion behind them .", arr_for_modified_train[0])
sentence3 = sentence_processing("I look forward to hearing your reply .", arr_for_modified_train[0])

value1 = log_probabilities_unigram(arr_for_modified_train[0], sentence1, arr_for_modified_train[1])
value2 = log_probabilities_unigram(arr_for_modified_train[0], sentence2, arr_for_modified_train[1])
value3 = log_probabilities_unigram(arr_for_modified_train[0], sentence3, arr_for_modified_train[1])
print(sentence1, ": ", value1)
print(sentence2, ": ", value2)
print(sentence3, ": ", value3)

# Log probabilities for Bigram
print("Bigram Log probabilities for Each sentence: ")
value_b_1 = log_probabilities_bigram(bigram_dictionary, unigram_dictionary, sentence1)
value_b_2 = log_probabilities_bigram(bigram_dictionary, unigram_dictionary, sentence2)
value_b_3 = log_probabilities_bigram(bigram_dictionary, unigram_dictionary, sentence3)

print(sentence1, ": ", value_b_1)
print(sentence2, ": ", value_b_2)
print(sentence3, ": ", value_b_3)

# Log probabilities for Bigram Smoothing add one
print("Bigram Add One smoothing Log probabilities for Each sentence: ")
value_smoothing_1 = bigram_add_smoothing(unigram_dictionary, bigram_dictionary, sentence1, len(unigram_dictionary))
print(sentence1, ": ", value_smoothing_1)
value_smoothing_2 = bigram_add_smoothing(unigram_dictionary, bigram_dictionary, sentence2, len(unigram_dictionary))
print(sentence2, ": ", value_smoothing_2)
value_smoothing_3 = bigram_add_smoothing(unigram_dictionary, bigram_dictionary, sentence3, len(unigram_dictionary))
print(sentence3, ": ", value_smoothing_3)

# Perplexity Unigram

print("Perplexity: ")
print("Perplexity Unigram: ")
unigram_value_perplexity_1 = unigram_perplexity(unigram_dictionary, sentence1, unigram_total_token)
print(sentence1, ": ", unigram_value_perplexity_1[0])
unigram_value_perplexity_2 = unigram_perplexity(unigram_dictionary, sentence2, unigram_total_token)
print(sentence2, ": ", unigram_value_perplexity_2[0])
unigram_value_perplexity_3 = unigram_perplexity(unigram_dictionary, sentence3, unigram_total_token)
print(sentence3, ": ", unigram_value_perplexity_3[0])

# Perplexity Bigram
print("Perplexity Bigram: ")
bigram_value_perplexity_1 = bigram_perplexity(unigram_dictionary, bigram_dictionary, sentence1)
print(sentence1, ": ", bigram_value_perplexity_1)
bigram_value_perplexity_2 = bigram_perplexity(unigram_dictionary, bigram_dictionary, sentence2)
print(sentence2, ": ", bigram_value_perplexity_2)
bigram_value_perplexity_3 = bigram_perplexity(unigram_dictionary, bigram_dictionary, sentence3)
print(sentence3, ": ", bigram_value_perplexity_3)

# Perplexity Bigram add one smoothing
print("Perplexity Bigram add one smoothing: ")
bigram_add_one_smoothing_1 = bigram_add_one_smoothing_perplexity(unigram_dictionary, bigram_dictionary, sentence1,
                                                                 len(unigram_dictionary))
print(sentence1, ": ", bigram_add_one_smoothing_1)
bigram_add_one_smoothing_2 = bigram_add_one_smoothing_perplexity(unigram_dictionary, bigram_dictionary, sentence2,
                                                                 len(unigram_dictionary))
print(sentence2, ": ", bigram_add_one_smoothing_2)
bigram_add_one_smoothing_3 = bigram_add_one_smoothing_perplexity(unigram_dictionary, bigram_dictionary, sentence3,
                                                                 len(unigram_dictionary))
print(sentence3, ": ", bigram_add_one_smoothing_3)

# Perplexity Brown-Test
print("Perplexity Brown-Test: ")

var1 = unique_word_token_for_unigram(brown_test_loader)
var2 = unique_word_token_for_unigram(learner_test_loader)

total_token_in_brown_test = var1[1]
total_token_in_learner_test = var2[1]

brown_test_value_unigram = unigram_perplexity_test_data(unigram_dictionary, brown_test_loader, unigram_total_token,
                                                        total_token_in_brown_test)
print("Brown Test Perplexity Unigram: ", brown_test_value_unigram)
