""" Trains models based on preprocessed inputs """
from textPreProcessing import *
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dropout, GlobalMaxPooling1D, Embedding, LSTM, Bidirectional, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model, Model

ENG_MODEL_PATH = 'models/eng_model'
UR_MODEL_PATH = 'models/test_ur_model2'
NUM_EPOCHS = 30

def getModel(totalWords, maxSequenceLen):
    ''' Returns neural network trained on corpus '''
    # Build Model
    model = Sequential()
    model.add(Embedding(totalWords, 240, input_length=maxSequenceLen - 1))
    model.add(Dropout(0.2))
    model.add(Bidirectional(LSTM(150)))
    model.add(Dense(totalWords, activation="softmax"))
    return model

def getModelTest(totalWords, maxSequenceLen):
    i = Input(shape=(maxSequenceLen - 1, ))
    x = Embedding(totalWords, 124)(i)
    x = Dropout(0.2)(x)
    x = LSTM(520, return_sequences=True)(x)
    x = Bidirectional(layer=LSTM(340, return_sequences=True))(x)
    x = GlobalMaxPooling1D()(x)
    x = Dense(1024, activation='relu')(x)
    x = Dense(totalWords, activation='softmax')(x)

    return Model(i,x)

def trainAndSaveModel(xs, ys, totalWords, maxSequenceLen, language):
    language = language.lower()
    if language != 'eng' and language != 'ur':
        raise ValueError

    model = getModel(totalWords, maxSequenceLen)
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    history = model.fit(xs, ys, epochs=NUM_EPOCHS, verbose=1)
    if language == 'eng':
        model.save(ENG_MODEL_PATH)
    elif language == 'ur':
        model.save(UR_MODEL_PATH)


def generateWords(model, seedText, language, numWords=100):
    language = language.lower()
    if language == 'eng':
        tokenizer = engTokenizer
        maxSequenceLen = maxEngSequenceLen
    elif language == 'ur':
        tokenizer = urTokenizer
        maxSequenceLen = maxUrSequenceLen
    else:
        raise ValueError

    for _ in range(numWords):
        tokenList = tokenizer.texts_to_sequences([seedText])[0]
        tokenList = pad_sequences([tokenList], maxlen=maxSequenceLen-1, padding='pre')
        predicted = model.predict_classes(tokenList, verbose=0)
        outputWord = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                outputWord = word
                break
        seedText += " " + outputWord
    return seedText + " "
    
# trainAndSaveModel(urXs, urYs, totalUrWords, maxUrSequenceLen, 'ur')
