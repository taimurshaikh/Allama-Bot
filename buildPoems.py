"""
    Builds Ghazal out of generated lines
    These are not true ghazals as they do not have a consistent rhyme scheme
    But the refrain phrase at the end of each sher is present
"""
import random
from google_trans_new import google_translator
from textPostProcessing import ENG_OUTPUT_FILE, UR_OUTPUT_FILE

# Pick sher count (5 to 15, but 7 most common)
# Build list of lists or dictionary of lines whos second last words rhyme, and last words are the same (refrain word)
# Pick random list X from this list
# For first sher, pick two lines from X
# For every following sher, pick random line, then pick line from X. Pair these together to create new sher
# Somewhat ensure all lines have same metre and syllabic length

POEMS_OUTPUT_FILE = "LOTPAnthology.txt"
TRANSLATED_OUTPUT_FILE = "LOTPAnthologyTranslated2.txt"

def main():
    with open(UR_OUTPUT_FILE, "r", encoding='utf-8') as f:
        generatedLines = list(set([x.strip() for x in f.readlines()]))
    # writeGhazalsToFile(generatedLines, POEMS_OUTPUT_FILE)
    print(buildGhazal(generatedLines))

def buildMatla(generatedLines):
    """
    The matla is a couplet where both lines end in the same refrain phrase.
    It is the first couplet in a ghazal
    """
    line1 = random.choice(generatedLines).split(' ')
    line2 = random.choice(generatedLines).split(' ')

    while line1 == line2 or line1[-2:] != line2[-2:] or line1[-1] == "e" or line2[-1] == "e":
        line1 = random.choice(generatedLines).split(' ')
        line2 = random.choice(generatedLines).split(' ')

    res =  [' '.join(line1).title(), ' '.join(line2).title()]
    return res

def buildSher(matla, generatedLines, prevLines=[]):
    """
    A sher(couplet) must have two lines. The second line must have the same refrain phrase as
    found in both lines of the matla
    """
    history = []
    if prevLines:
        for sher in prevLines:
            for line in sher:
                history.append(line.strip())
    refrain = matla[0].split(' ')[-2:]

    line1 = random.choice(generatedLines).split(' ')
    line2 = random.choice(generatedLines).split(' ')

    while line1 == line2 or line1[-2:] == refrain or line2[-2:] != refrain or line1[-1] == "e" or line2[-1] == "e" or ' '.join(line1).strip() in history or ' '.join(line2).strip() in history:
        line1 = random.choice(generatedLines).split(' ')
        line2 = random.choice(generatedLines).split(' ')

    res =  [' '.join(line1).title(), ' '.join(line2).title()]
    return res


def buildGhazal(generatedLines):
    sherCount = random.choices([x for x in range(5,16)], weights=[0.5] * 2 + [1] + [0.5 for x in range(8)])[0]
    ghazal = []
    matla = buildMatla(generatedLines)
    ghazal.append(matla)

    for i in range(sherCount - 1):
        ghazal.append(buildSher(matla, generatedLines, ghazal))
    return ghazal

def writeGhazalsToFile(generatedLines, path, numGhazals=50, numExistingGhazals=0):
    with open(path, "a", encoding="utf-8") as f:
        for i in range(numExistingGhazals - 1 if numExistingGhazals else 0, numGhazals):
            f.write("\n")
            f.write(str(i + 1) + ":\n")
            ghazal = buildGhazal(generatedLines)
            for sher in ghazal:
                for line in sher:
                    f.write(line.strip())
                    f.write("\n")
                f.write("\n")

def translateGhazals(inPath, outPath):
    translator = google_translator()
    translation = []
    with open(inPath, "r", encoding="utf-8") as inputFile:
        fileContents = inputFile.readlines()
        for line in fileContents:
            if line != "\n":
                translation.append(translator.translate(line, lang_src="ur", lang_tgt="en") + "\n")
            else:
                translation.append("\n")
    # for line in translation:
    #     print(line)

    with open(outPath, "w+", encoding="utf-8") as f:
        for line in translation:
            f.write(line)





# poem = []
# with open(UR_OUTPUT_FILE, "r", encoding='utf-8') as f:
#     lines = f.readlines()
#     for i in range(7):
#         sher = []
#         for j in range(2):
#             sher.append(random.choice(lines))
#         poem.append(sher)
# for sher in poem:
#     for line in sher:
#         print(line.strip(), end='\n')
#     print()

if __name__ == "__main__":
    main()
