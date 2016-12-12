import collections
from wordlist_corner_case_tokenize import wordlist_corner_case_tokenize as list_process
from nltk import word_tokenize, sent_tokenize
from find_sent import find_sent


def count_sent_len(sent_len_statistics, rawdata):
    sent_len_distribution = open('sent_len_distribution.txt', 'w')
    cnt = 0
    len_counter = collections.Counter()
    for topic_data in rawdata['data']:
        for paragraph in topic_data['paragraphs']:
            len_cnt = len(sent_tokenize(paragraph['context']))
            print(cnt, len_cnt, file=sent_len_statistics)
            len_counter[str(len_cnt)] += 1
            # print(sent_tokenize(paragraph['context']))
            cnt += 1
            if cnt > 18890:
                print(sent_tokenize(paragraph['context']))
    for i, c in len_counter.most_common():
        print(i, c, file=sent_len_distribution)
