#!/bin/bash/python3

from phonesimilarity import phone, similarity;
p1 = phone('AE')
p2 = phone('SIL')

s = similarity()
sim = s.cosinesimilarity('AE', 'SIL')
print(sim)
