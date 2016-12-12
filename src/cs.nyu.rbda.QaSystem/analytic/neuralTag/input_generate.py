import json
import collections
from wordlist_corner_case_tokenize import wordlist_corner_case_tokenize as list_process
from nltk import word_tokenize, sent_tokenize


dataset = open('train-v1.1.json', 'r')
rawdata = json.load(dataset)


def tokenize(line):
    return [s.lower() for s in word_tokenize(line)]


squad_tagged_input = open('squad_tagged_input.txt', 'w')

for topic_data in rawdata['data']:
    for paragraph in topic_data['paragraphs']:
        sent_list = sent_tokenize(paragraph['context'])
        for sent in sent_list:
            for word in list_process(tokenize(sent)):
                print(word, file=squad_tagged_input)
            print('\n', file=squad_tagged_input)
