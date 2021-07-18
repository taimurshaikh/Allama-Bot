""" Takes output text from model and generates lines """
from nlpModel import *
import syllables
import random

ENG_START_WORDS_FILE = "start words/engStartWords.txt"
UR_START_WORDS_FILE = "start words/urStartWords.txt"
ENG_OUTPUT_FILE = "generated/eng.txt"
UR_OUTPUT_FILE = "generated/testur.txt"

# Start Words files Iqbal would start lines with + first words of each line of the corpus
with open(UR_START_WORDS_FILE, "r") as f:
    UR_START_WORDS = f.read().split('\n')

with open(ENG_START_WORDS_FILE, "r") as f:
    ENG_START_WORDS = f.read().split('\n')

WORDS_PER_START_WORD = 10
AVG_UR_SYLLABLES = sum([syllables.estimate(line) for line in urCorpus]) // len(engCorpus)

def main():
    language = 'ur'
    if language == 'eng':
        model = load_model(ENG_MODEL_PATH)
    elif language == 'ur':
        model = load_model(UR_MODEL_PATH)
    else:
        raise ValueError

    writeLinesToFile(model, language, UR_OUTPUT_FILE, UR_START_WORDS)

def writeLinesToFile(model, lang, filePath, startWords):
    textString = ""

    for word in startWords:
            textString += generateWords(model, word, lang, WORDS_PER_START_WORD) + '\n'

    # The model tends to repeat two word phrases such as 'mujh ko' consecutively. To refine the text a little bit, we can do some post processng, whilst not altering the model's output too drastically
    textString = removeDuplicatePhrases(textString)
    lines = textString.split('\n')

    with open(filePath, "a", encoding='utf-8') as f:
        for line in lines:
            f.write(line.strip())
            f.write("\n")

def removeDuplicatePhrases(text):
    """ Removes one and two word duplicates from text, as well as a word repeating very other word """
    textLst = text.split(' ')
    for i in range(len(textLst)):
        if i == len(textLst) - 1:
            break
        # Remove one word duplicates:
        elif textLst[i] == textLst[i+1]:
            textLst.pop(i)

        if i == len(textLst) - 2:
            break
        # Remove two word duplicates
        elif textLst[i:i+2] == textLst[i+2: i+4]:
            textLst.pop(i)
            textLst.pop(i+1)

        # Removing alternating repeating words
        if textLst[i] == textLst[i+2]:
            textLst.pop(i+2)

    return ' '.join(textLst)

def splitIntoLines(text, syllablesPerLine=AVG_UR_SYLLABLES, rangeOfVals=2, numLines=7):
    """ Splits block of text into list of lines with ROUGHLY the same amount of syllables """
    textLst = text.split(' ')
    lines = []
    currentLine = ""
    currentSyllables = 0
    for word in textLst:
        currentSyllables += syllables.estimate(word)
        currentLine += " " + word
        # We don't want to end a line on e (of)
        if word.strip().lower() == 'e':
            continue
        if currentSyllables >= syllablesPerLine:
            lines.append(currentLine)
            currentLine = ""
            currentSyllables = 0

    return lines

def splitByStartWord():
    pass
#
# with open("newnew.txt", "w", encoding='utf-8') as f, open("new.txt", "r", encoding='utf-8') as g:
#     lines = set(g.readlines())
#     for line in lines:
#         f.write(line)
#
if __name__ == '__main__':
     main()
