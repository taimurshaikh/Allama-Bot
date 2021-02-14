''' Builds Ghazal out of generated lines '''
import random
# Pick sher count (5 to 15, but 7 most common)
# Build list of lists of lines whos second last words rhyme, and last words are the same (refrain word)
# Pick random list X from this list
# For first sher, pick two lines from X
# For every following sher, pick random line, then pick line from X. Pair these together to create new sher
# Somewhat ensure all lines have same metre and syllabic length
def buildGhazal(generatedLines):
    sherCount = random.choices([x for x in range(5,16)], weights=[0.5] * 2 + [1] + [0.5 for x in range(8)])
    print(sherCount)
buildGhazal()
