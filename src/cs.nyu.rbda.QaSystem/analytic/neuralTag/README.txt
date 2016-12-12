###### input data source:
	1. en-wsj-train.pos , https://github.com/robertsdionne/nlp/tree/master/data
	2. en-wsj-dev.pos , https://github.com/robertsdionne/nlp/tree/master/data
	3. train-v1.1.json , https://rajpurkar.github.io/SQuAD-explorer/ where the "Training Set v1.1" is the one

###### expected outputs:
	1. squad_tagged_input.txt , which is essentially a intermediate file used as input to the neuralTagger.py
	2. squad_tagged_output.txt , final output, which have each word of squad paired with its POS tag

###### code description:
  1. input_generate.py, generate the expected output#1
  2. neuralTagger.py, generate the expected output#2, the main part
  3. ./lib/mio.py, does the I/O related util work
  4. ./lib/tagger.py, core tagger part part used in neuralTagger.py
  5. ./lib/util.py, does the padding job to make sentence to the same length

###### guide to run:
  1. generate squad_tagged_input.txt for subsequent use
  $ python3 input_generate.py
  2. run tagger
  $ python3 neuralTagger.py
  
notes: 
  1. make sure you have 1)tensorflow and 2)keras properly installed for python3
  2. sometimes it raises some errors but not every time, it doesn’t hurt the final output! This is a version issue of libraries’ supporting python3 compatibility, which haven’t been resolved by the community, here has a issue discussion: https://github.com/tensorflow/tensorflow/issues/3388.

##### screenshot:
	shows the bash output when neuralTagger.py is training successfully, you will have a similar bash output depending on hyperparameters you want to set. typically it takes almost 5 hours to run on a machine like: 2.7 GHz Intel Core i5, 8 GB 1867 MHz DDR3.
