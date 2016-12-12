def find_sent(l, ans_start):
    if len(l) == 1:
        return 0
    else:
        tmp = 0
        for i, element in enumerate(l):
            if tmp+len(element) > ans_start:
                return i
            tmp += len(element)+1 # add 1 because of the delimiter ' ' between tokenized sentence
