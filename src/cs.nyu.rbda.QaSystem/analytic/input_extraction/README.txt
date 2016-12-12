###### input data source:
	1. train-v1.1.json , https://rajpurkar.github.io/SQuAD-explorer/ where the "Training Set v1.1" is the one
	2. squad_words.txt , which is one of the outputs from the ../preprocessing/ folder

###### expected outputs:
	1. ans_sent_pointer.txt, which contains the sent index where the answer appears in the context
	2. sent_len_statistics.txt, which contains the sentence length statistics for all the sentences in the context
  3. words_per_doc_distribution.txt, which contains the #words distribution of each context in the training set
  4. words_per_sent_distribution.txt, which contains the #words distribution of each sentence in the training set

###### code description:
  1. ans_pointers_generate.py, generate the expected output#1
  2. count_sent_len.py, generate the expected output#2
  3. find_sent.py, util function
	4. wordlist_corner_case_tokenize.py, fine grained tokenizer on top of nltk's tokenizer
  5. harness.py, puts things together

###### guide to run:
  $ python3 harness.py
  notes: make sure you have nltk properly installed for python3

##### screenshot:
	shows the bash output when harness.py run successfully
