#!/bin/bash/python3

from scipy import spatial
import csv
import numpy as np

class phone:
    def __init__(self, phone):
        phone = phone.upper()
        ftable = open('spe_features_zeros.csv', 'r')
        #ftable = open('sampel_feat.csv', 'r')
        reader = csv.reader(ftable)
        self.header = next(reader)
        feature_lenght = len(self.header) - 1  
        z = [0] 
        self.features = z * feature_lenght
        phone_list = []
        for line in reader:
            phone_list.append(line[0])
            if(line[0] == phone):
                self.features = line[1:len(line)]
        if phone not in phone_list:
            raise ValueError("Oops! phone {} not in the list".format(phone))

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
        return round(1.0 - spatial.distance.cosine(p1f, p2f),3)


    def normsimilarity(sefl, p1, p2):
        phone1 = phone(p1)
        phone2 = phone(p2)
        p1f = np.array(phone1.getfeatures())
        p2f = np.array(phone2.getfeatures())
        correct_matches = sum(i > 0 for i in list(p1f & p2f))
        return correct_matches/len(p1f)
