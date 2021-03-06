""" Builds Ghazal out of generated lines """
import random
from textPostProcessing import ENG_OUTPUT_FILE, UR_OUTPUT_FILE

# Pick sher count (5 to 15, but 7 most common)
# Build list of lists or dictionary of lines whos second last words rhyme, and last words are the same (refrain word)
# Pick random list X from this list
# For first sher, pick two lines from X
# For every following sher, pick random line, then pick line from X. Pair these together to create new sher
# Somewhat ensure all lines have same metre and syllabic length

def buildMatla():
    pass

def buildSher():
    pass

def buildGhazal(generatedLines):
    sherCount = random.choices([x for x in range(5,16)], weights=[0.5] * 2 + [1] + [0.5 for x in range(8)])

def buildRhymeDict():
    # This dict is like an adjacency list: {0:[1, 2, 3]} means line 0 rhymes with lines 1 2 and 3
    rhymes = {}

poem = []
with open(ENG_OUTPUT_FILE, "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(7):
        sher = []
        for j in range(2):
            sher.append(random.choice(lines))
        poem.append(sher)
for sher in poem:
    for line in sher:
        print(line.strip(), end='\n')
    print()
