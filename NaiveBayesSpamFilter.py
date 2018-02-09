'''
LANGUAGE:
 Python3

TRAINING DATASET:
 Input file should have three fields delimited by a single space: word spam_count not_spam_count

TESTING DATASET:
 Input file should have the contents of a given email

OUTPUT:
 Given testing dataset should be classified as "spam" or "not spam"

'''

import re
import math

class NaiveBayesSpamFilter():
    # probabilities = map(word, ( p(word | spam), p(word | ~spam))
    probabilities = {}

    def train(self, input):
        words = {}
        spam = []
        not_spam = []
        total_spam = total_not_spam = 0
        index = 0

        with open(input, 'r', encoding="utf-8") as f:
            for line in f:
                word, spam_count, not_spam_count = line.split(" ")
                total_spam += int(spam_count)
                total_not_spam += int(not_spam_count)

                if word in words:
                    idx = words[word]
                else:
                    words[word] = index
                    spam.append(0)
                    not_spam.append(0)
                    idx = index
                    index += 1
                spam[idx] += int(spam_count)
                not_spam[idx] += int(not_spam_count)

        for w in words:
            index = words[w]
            self.probabilities[w] = (spam[index]/total_spam,
                                     not_spam[index]/total_not_spam)

    def classify(self, input):
        words = self.extract_email_words(input)
        log_spam = log_not_spam = 0.0
        for w in words:
            if w in self.probabilities:
                log_spam += math.log(self.probabilities[w][0])
                log_not_spam += math.log(self.probabilities[w][1])

        print("log_spam = ", log_spam)
        print("log_not_spam = ", log_not_spam)

        if log_spam > log_not_spam:
            return "spam"
        return "not spam"


    def extract_email_words(self, input):
        words = set()

        with open(input, 'r', encoding="utf-8") as f:
            for line in f:
                lineWords =  re.findall("[a-z']+", line.lower())
                words.update(lineWords)
        return words


training = input("path to training dataset: ")
testing = input("path to testing dataset: ")

v = NaiveBayesSpamFilter()
v.train(training)
print("Classification = ", v.classify(testing))


