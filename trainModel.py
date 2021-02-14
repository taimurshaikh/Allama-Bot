''' Training script '''
import textPreProcessing
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Bidirectional, Dense
from tensorflow.keras.optimizers import Adam

inputs = textPreProcessing.inputs
total_words = textPreProcessing.total_words
max_sequence_len = textPreProcessing.max_sequence_len

xs = inputs[:,:-1]
labels = inputs[:,-1]
ys = to_categorical(labels, num_classes=total_words)

def train_model():
    ''' Returns neural network trained on corpus '''
    # Build Model
    model = Sequential()
    model.add(Embedding(total_words, 240, input_length=max_sequence_len - 1))
    model.add(Bidirectional(LSTM(150)))
    model.add(Dense(total_words, activation="softmax"))
    adam = Adam(lr=0.01)

    # Compile and fit model
    model.compile(loss="categorical_crossentropy", optimizer=adam, metrics=["accuracy"])
    history = model.fit(xs, ys, epochs=100, verbose=1)

    # Save model
    model.save('C:/Users/taimu/GitHub/Allama-Bot/models')
