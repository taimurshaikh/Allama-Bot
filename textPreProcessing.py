""" Preprocceses text by performing linguistic techniques to generate model inputs """
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from random import shuffle

engCorpus = []
urCorpus = []
startWords = set()
# File handling
with open("books-1-2-3-4/books-1-2-3-4.en", encoding='utf-8') as eng, open("books-1-2-3-4/books-1-2-3-4.ro", encoding='utf-8') as ur:
    for engLine, urLine in zip(eng, ur):
        if len(urLine.split(' ')) == 1:
            continue
        engCorpus.append(engLine.strip())
        urCorpus.append(urLine.strip())

        startWords.add(urLine.split(' ')[0])

shuffle(engCorpus)
shuffle(urCorpus)

engTokenizer = Tokenizer(filters='-',lower=False)
urTokenizer = Tokenizer(filters='-', lower=False)

# Create word index for both corpi
engTokenizer.fit_on_texts(engCorpus)
urTokenizer.fit_on_texts(urCorpus)

# 1 is added for the OOV token
totalEngWords = len(engTokenizer.word_index) + 1
totalUrWords = len(urTokenizer.word_index) + 1

def generateInputs(corpus, tokenizer):
    """ Generates input data from tokenizer """
    inputs = []
    # Creating n-gram data
    for line in corpus:
        tokenList = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(tokenList)):
            nGram = tokenList[:i+1]
            inputs.append(nGram)

    maxSequenceLen = max([len(_) for _ in inputs])
    inputs = np.array(pad_sequences(inputs, maxlen=maxSequenceLen, padding='pre'))
    return (inputs, maxSequenceLen)

engLines = generateInputs(engCorpus, engTokenizer)
engInputs = engLines[0]
maxEngSequenceLen = engLines[1]

urLines = generateInputs(urCorpus, urTokenizer)
urInputs = urLines[0]
maxUrSequenceLen = urLines[1]

engXs = engInputs[:,:-1]
engLabels = engInputs[:,-1]
engYs = to_categorical(engLabels, num_classes=totalEngWords)

urXs = urInputs[:,:-1]
urLabels = urInputs[:,-1]
urYs = to_categorical(urLabels, num_classes=totalUrWords)
