###### input data source: 
	1. http://nlp.stanford.edu/projects/glove/ , where the “glove.6B.50d.txt” is the one
	2. squad_words.txt , which is one of the outputs from the ../preprocessing/ folder

###### expected outputs:
	1. glove_words.txt, containing all the words in the glove_words.txt which includes word embeddings
	2. intersection.txt, which contains the words that are in the intersection between squad_words.txt and glove.6B.50d.txt files

###### code description:
	1. load_hdfs.sh		load glove.6B.50d.txt into hdfs
	2. glove_word_extract	scala cmd line codes, extracts words in the embedding file, glove.6B.50d.txt
	3. find_intersection	scala cmd line codes, extract intersection of squad_words and glove_words

###### guide to run:
	run the three files in the code description section in the same order, the find_intersection file depends on the output of glove_word_extract

