#!/bin/bash/python3
import numpy as np
import csv
import matplotlib.pyplot as plt
import os

from phonesimilarity import phone, distance;

dis = distance().jaccardDistance
#dis = distance().simpleMatchingDistance

ftable = open('spe_features_zeros.csv', 'r')
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
        cmatrix[i][j] = dis(f,g)
        #print("smd of {} and {} is {}".format(f, g, dis(f,g)))

mat = np.array(cmatrix)
mini = np.min(mat, axis=0)
maxi = np.max(mat, axis= 0)
print(min(mini))
print(max(maxi))

figuredir = 'figures'
if not os.path.exists(figuredir):
    os.mkdir(figuredir)

print("Saving plot in figures directory")
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)
heatmap = ax.pcolor(cmatrix, cmap=plt.cm.Blues)
cbar = plt.colorbar(heatmap, fraction=0.02, pad=0.02)
ax.set_title('Cost for each pair of phones shown as heat-map')
ax.set_xticks(np.arange(len(cmatrix)) + 0.5, minor=False)
ax.set_yticks(np.arange(len(cmatrix)) + 0.5, minor=False)
ax.set_xticklabels(list(phones_list), minor=False, fontsize=4)
ax.set_yticklabels(list(phones_list), minor=False, fontsize=4)
filename = os.path.join(figuredir, ftable.name.split(".")[0] + '_' +dis.__name__ + '.pdf')
plt.savefig(filename, format='pdf')
