import collections
from wordlist_corner_case_tokenize import wordlist_corner_case_tokenize as list_process
from nltk import word_tokenize, sent_tokenize
from find_sent import find_sent


def ans_pointers_generate(ans_sent_pointer, rawdata):
    for topic_data in rawdata['data']:
        for paragraph in topic_data['paragraphs']:
            sent_list = sent_tokenize(paragraph['context'])
            for i, qa in enumerate(paragraph['qas']):

                tmp = {}
                tmp[i] = list()
                for answer in qa['answers']:
                    ans_start = answer['answer_start']
                    tmp[i].append(find_sent(sent_list, ans_start))
                for q_index, value in tmp.items():
                    ans_sent_pointer.write(str(q_index))
                    ans_sent_pointer.write(':')
                    for j in value:
                        ans_sent_pointer.write(str(j))
                        ans_sent_pointer.write(' ')
            ans_sent_pointer.write('\n')
