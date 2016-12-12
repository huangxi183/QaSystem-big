###### main codes description:
  1. model_train.py , which is the training model harness
  2. SentenceClassifier.py , which score the sentences from context
  3. attention.py , which implement the attention mechanism for the model , https://arxiv.org/abs/1409.0473
  4. rnn_cell.py , which instantiate an rnn_cell unit
  5. rnn.py , which creates an rnn layer
  6. other codes and files are for utilities

###### guide to run:
  $ python3 model_train.py

  notes: make sure you have tensoreflow and nltk properly installed for python3

##### screenshot:
	shows the output when model_train.py training successfully, where prints the training loss and dev accuracy at each checkpoint for verification.
