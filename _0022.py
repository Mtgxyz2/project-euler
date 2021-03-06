#!/usr/bin/env python3
# cython: language_level=3
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
import json
with open("data/names.json") as f:
    names = json.load(f)

names = sorted(names)
rankcount = 0
for n in range(len(names)):
    rank = (n + 1) * sum((ord(i) - 0x40 for i in names[n]))
    rankcount += rank
print(rankcount)
