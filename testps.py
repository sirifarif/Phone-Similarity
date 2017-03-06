#!/bin/bash/python3

from ps import phone, similarity;
p1 = phone('AE')
p2 = phone('SIL')

s = similarity()
sim = s.cosinesimilarity('AE', 'SIL')
print(sim)
sim = s.normsimilarity('SIL','SIL')
print(sim)
