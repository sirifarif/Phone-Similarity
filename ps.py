#!/bin/bash/python3

from scipy import spatial
import csv
import numpy as np

class phone:
    def __init__(self, phone):
        ftable = open('spe_features.csv', 'r')
        reader = csv.reader(ftable)
        self.header = next(reader)
        feature_lenght = len(self.header) - 1  
        z = [0] 
        self.features = z * feature_lenght
        for line in reader:
            if(line[0] == phone):
                self.features = line[1:len(line)]

    def getfeatures(self):
        return list(map(int, self.features))
    
    def setfeature(self, feature):
        index = self.header.index(feature)
        self.features[index-1] = 1

    def unsetfeature(self, feature):
        index = self.header.index(feature)
        self.features[index-1] = 0

class similarity:

    def cosinesimilarity(self, p1,p2):
        phone1 = phone(p1)
        phone2 = phone(p2)
        p1f = phone1.getfeatures()
        p2f = phone2.getfeatures()
        return 1.0 - spatial.distance.cosine(p1f, p2f)


#    def normsimilarity(sefl, p1, p2):
#        phone1 = phone(p1)
#        phone2 = phone(p2)
#        p1f = np.array(phone1.getfeatures())
#        p2f = np.array(phone2.getfeatures())
#        correct_matches = sum(i > 0 for i in list(p1f & p2f))
#        print(correct_matches)
#        return correct_matches/len(p1f)
