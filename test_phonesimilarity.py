#!/bin/bash/python3
import numpy
import csv
import matplotlib.pyplot as plt

from phonesimilarity import phone, similarity;
p1 = phone('AE')
p2 = phone('SIL')

s = similarity()
sim = s.cosinesimilarity('AE', 'SIL')
print(sim)

#ftable = open("sampel_feat.csv", "r")
ftable = open("spe_features.csv", "r")
reader = csv.reader(ftable)
next(reader)
phones_list = []
for l in reader:
    phones_list.append(l[0])
w, h = len(phones_list), len(phones_list)
cmatrix = [[0 for x in range(w)] for y in range(h)]

for i, f in enumerate(phones_list):
    for j, g in enumerate(phones_list):
        cmatrix[i][j] = round(s.cosinesimilarity(f,g),3)

print("DEBIG")
fig = plt.figure(figsize=(8, 4.2))
ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(cmatrix, origin='lower', interpolation='nearest')
plt.xticks(range(len(phones_list)), phones_list, size=2)
plt.yticks(range(len(phones_list)), phones_list, size=2)
plt.savefig("test.png", format="png", dpi= 500)
