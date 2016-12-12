from lib.tagger import SequenceTagger
from keras.models import Model, Sequential
from keras.layers import Dense, Input, Activation
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import TimeDistributed
from keras.layers.embeddings import Embedding


class BasicSequenceTagger(SequenceTagger):

    def __init__(self):
        ########################graph architechture
        self.in_dim=100
        self.h_dim=100
        ########################

    def build_graph(self):
        self.model = Sequential()
        self.model.add(Embedding(self.get_num_features(), self.in_dim,
                                 input_length=self.max_sentence_len, mask_zero=True))
        ###################################graph architechture
        self.model.add(LSTM(self.h_dim, return_sequences=True))
        #self.model.add(LSTM(self.h_dim, return_sequences=True))
        self.model.add(TimeDistributed(Dense(self.get_num_tags())))
        self.model.add(Activation('sigmoid'))
        ###################################
        self.model.compile(loss='categorical_crossentropy', optimizer='adam',
                           metrics=['accuracy'])

# create tagger and read data
tagger = BasicSequenceTagger()

#########################data input and output
tagger.read_data("en-wsj-train.pos", "squad_tagged_input.txt","en-wsj-dev.pos")
#########################

print("Building model")
tagger.build_graph()
print("Training..")
#########################training setting
batch_size=32
epochs=20
#########################
tagger.fit(batch_size, epochs)

tagger.predict(tagger.test_X, "squad_tagged_output.txt")
