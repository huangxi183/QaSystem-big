###### input data source:
	1. train-v1.1.json , https://rajpurkar.github.io/SQuAD-explorer/ where the "Training Set v1.1" is the one

###### expected outputs:
	1. squad_words.txt, which contains all the tokens after tokenized

###### code description:
	1. extract_squad_words.py, which does the main job
	2. wordlist_corner_case_tokenize.py, fine grained tokenizer built on top of nltk’s tokenizer

###### guide to run:
  $ python3 extract_squad_words.py
  notes: make sure you have nltk properly installed for python3