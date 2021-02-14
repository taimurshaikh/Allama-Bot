"Tokenizes raw English and Urdu text"
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# PIPELINE FOR PROJECT
# Pick between English or Urdu
# Train model on corresponding set of lines (save model)
# Generate set of new lines
# Build Ghazals out of generated lines

engLines = []
urLines = []
with open("books-1-2-3-4/books-1-2-3-4.en", encoding='utf-8') as eng, open("books-1-2-3-4/books-1-2-3-4.ro", encoding='utf-8') as ur:
    for engLine, urLine in zip(eng, ur):
        engLines.append(engLine)
        urLines.append(urLine)

engTokenizer = Tokenizer()
urTokenizer = Tokenizer()

engCorpus = engLines
urCorpus = urLines

engTokenizer.fit_on_texts(engCorpus)
urTokenizer.fit_on_texts(urCorpus)

total_eng_words = len(engTokenizer.word_index) + 1
total_ur_words = len(urTokenizer.word_index) + 1

def generateInputs(corpus, tokenizer):
    inputs = []
    # Creating n-gram data
    for line in engCorpus:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram = token_list[:i+1]
            inputs.append(n_gram)

    max_sequence_len = max([len(_) for _ in inputs])
    inputs = np.array(pad_sequences(inputs, maxlen=max_sequence_len, padding='pre'))
    return (inputs, max_sequence_len)
