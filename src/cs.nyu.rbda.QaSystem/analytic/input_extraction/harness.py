import json
import collections
from wordlist_corner_case_tokenize import wordlist_corner_case_tokenize as list_process
from nltk import word_tokenize, sent_tokenize
from count_sent_len import count_sent_len
from ans_pointers_generate import ans_pointers_generate
from find_sent import find_sent

dataset = open('train-v1.1.json', 'r')
rawdata = json.load(dataset)




def tokenize(line):
    return [s.lower() for s in word_tokenize(line)]



word_counter = collections.Counter()
sent_counter = {}
sent_count_stat = collections.Counter()
ans_sent_indexer = {}
context_counter = {}

#
# sent_len_statistics = open('sent_len_testout.txt', 'w')
# count_sent_len(sent_len_statistics)
# for topic_data in rawdata['data']:
#     context_counter[topic_data['title']] = len(topic_data['paragraphs'])
#
# context_topic_statistics = open('context_topic_statistics.txt', 'w')
# context_topic_statistics.write('\n'.join('%s %s' % x for x in context_counter.items()))


# sent_len_statistics = open('sent_len_statistics.txt', 'w')
# sent_len_statistics.write('\n'.join('%s %s' % x for x in sent_counter.items()))
#
# sent_count_stat.update(sent_counter)
# sent_count_stat_output = open('sent_count_statistics.txt', 'w')
# sent_count_stat_output.write('\n'.join('%s %s' % x for x in sent_count_stat.most_common()))
# test_sent = 'Super Bowl 50 was an American football game to determine the champion of the National Football League (NFL) for the 2015 season. The American Football Conference (AFC) champion Denver Broncos defeated the National Football Conference (NFC) champion Carolina Panthers 24\u201310 to earn their third Super Bowl title. The game was played on February 7, 2016, at Levi\'s Stadium in the San Francisco Bay Area at Santa Clara, California. As this was the 50th Super Bowl, the league emphasized the \"golden anniversary\" with various gold-themed initiatives, as well as temporarily suspending the tradition of naming each Super Bowl game with Roman numerals (under which the game would have been known as \"Super Bowl L\"), gold-colored so that the logo could prominently feature the Arabic numerals 50.'
# # l = tokenize(test_sent)


words_per_doc_distribution = open('words_per_doc_distribution.txt', 'w')
words_per_sent_distribution = open('words_per_sent_distribution.txt', 'w')
sent_len_statistics = open('sent_len_statistics.txt', 'w')
ans_sent_pointer = open('ans_sent_pointer.txt', 'w')
count_sent_len(sent_len_statistics, rawdata)
ans_pointers_generate(ans_sent_pointer, rawdata)

doc_index = 0
sent_index = 0
doc_words_max = 0
sent_words_max = 0
doc_words = collections.Counter()
sent_words = collections.Counter()
debug_flag = False

for topic_data in rawdata['data']:
    for paragraph in topic_data['paragraphs']:
        l = len(list_process(tokenize(paragraph['context'])))
        doc_words.update([str(l)])
        if doc_words_max < l:
            doc_words_max = l

        for sent in sent_tokenize(paragraph['context']):
            l = len(list_process(tokenize(sent)))
            sent_words.update([str(l)])
            if l > 200 :
                if debug_flag == False:
                    print(list_process(tokenize(sent)))
                    debug_flag = True

            if sent_words_max < l:
                sent_words_max = l

for i, j in doc_words.most_common():
    print(j, i, file=words_per_doc_distribution)


for i, j in sent_words.most_common():
    print(j, i, file=words_per_sent_distribution)

print('max #words in a doc: ', doc_words_max)
print('max #words in a sent: ', sent_words_max)
