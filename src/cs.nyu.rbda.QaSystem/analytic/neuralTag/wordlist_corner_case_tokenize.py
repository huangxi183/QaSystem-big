import re
import itertools


def digit_to_N(word):
    # 3.3 => N; 3,33.3 =>NNN
    if re.match(r'^(\d+([.]|[,]))*\d+$', word):
        word = re.sub(r'[,]', '', word)
        integer_len = len(re.match(r'^\d+', word).group())
        return 'N'*integer_len if integer_len <= 5 else 'NNNNN'
    # 333333 => NNNNN
    elif re.match(r'^\d+$', word):
        word_len = len(word)
        return 'N'*word_len if word_len <= 5 else 'NNNNN'
    # 3,333 => NNNN
    # elif re.match(r'^(\d+[,])*\d+$', word):
    #     word_len = len(re.sub(r'[,]', '', word))
    #     return 'N' * word_len if word_len <= 5 else 'NNNNN'
    else:
        return word


def seperate_dash_colon(word):
    # re.match(r'^(.*[-].*)\1*')
    return re.sub(r'[:]', ' : ', re.sub(r'-|—|–|_', ' - ', word))


def seperate_slash_backslash(word):
    return re.sub(r'[/]', ' / ', re.sub(r'[\\]', ' \\ ', word))


def word_corner_case_tokenize(word):
    word = seperate_dash_colon(word)
    word = seperate_slash_backslash(word)
    return [digit_to_N(w) for w in word.split()]


def wordlist_corner_case_tokenize(wordlist):
    return list(itertools.chain.from_iterable([word_corner_case_tokenize(word) for word in wordlist]))