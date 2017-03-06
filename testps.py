#!/bin/bash/python3

from ps import phone, similarity;
p = phone('Z')
print(p.getfeatures())

p = phone('X')
print(p.getfeatures())

print("DEBUG")
s = similarity()
print("XXX")

print(s.cosinesimilarity('A', 'X'))

print(s.cosinesimilarity('A', 'E'))

print("cosine sim for U Z {}".format(s.cosinesimilarity('U', 'Z')))
