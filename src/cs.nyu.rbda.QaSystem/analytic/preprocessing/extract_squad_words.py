import json
import collections
from wordlist_corner_case_tokenize import wordlist_corner_case_tokenize as list_process
from nltk import word_tokenize, sent_tokenize

dataset = open('train-v1.1.json', 'r')
rawdata = json.load(dataset)


def tokenize(line):
    return [s.lower() for s in word_tokenize(line)]


word_counter = collections.Counter()

squad_words = open('squad_words.txt', 'w')

for topic_data in rawdata['data']:
    for paragraph in topic_data['paragraphs']:
        l = list_process(tokenize(paragraph['context'])))
        word_counter.update(l)

for word, _ in word_counter.most_common():
    print(word, file=squad_words)
