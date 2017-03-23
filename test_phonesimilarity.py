#!/bin/bash/python3
import numpy as np
import csv
import matplotlib.pyplot as plt

from phonesimilarity import phone, similarity;

sim = similarity().cosinesimilarity

ftable = open('spe_features.csv', 'r')
#ftable = open('sampel_feat.csv', 'r')
reader = csv.reader(ftable)
next(reader)
phones_list = []
for l in reader:
    phones_list.append(l[0])
w, h = len(phones_list), len(phones_list)
cmatrix = [[0 for x in range(w)] for y in range(h)]

for i, f in enumerate(phones_list):
    for j, g in enumerate(phones_list):
        cmatrix[i][j] = sim(f,g)
print("Saving Image")
fig = plt.figure(figsize=(8, 4.2))
ax = fig.add_subplot(111)
heatmap = ax.pcolor(cmatrix, cmap=plt.cm.Blues)
cbar = plt.colorbar(heatmap)
ax.set_title('phone to phone similarity')
ax.set_xticks(np.arange(len(cmatrix)) + 0.5, minor=False)
ax.set_yticks(np.arange(len(cmatrix)) + 0.5, minor=False)
ax.set_xticklabels(list(phones_list), minor=False, fontsize='small')
ax.set_yticklabels(list(phones_list), minor=False, fontsize='small')
plt.savefig(ftable.name.split(".")[0] + ".png", format="png", dpi= 500)
