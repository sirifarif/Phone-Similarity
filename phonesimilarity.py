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

class distance:

    def cosineDistance(self, p1,p2):
        phone1 = phone(p1)
        phone2 = phone(p2)
        p1f = phone1.getfeatures()
        p2f = phone2.getfeatures()
        return round(spatial.distance.cosine(p1f, p2f),3)

    def jaccardDistance(self, p1,p2):
        phone1 = phone(p1)
        phone2 = phone(p2)
        p1f = phone1.getfeatures()
        p2f = phone2.getfeatures()
        return round(spatial.distance.jaccard(p1f, p2f),3)

    '''
    instead of true or false we take each feature and its complement at the same time.
    For example as nasal and not-nasal
    '''
    def jaccardSymetricDistance(self, p1,p2):
        phone1 = phone(p1)
        phone2 = phone(p2)
        p1f = np.asarray(phone1.getfeatures()).astype(np.bool)
        p1fnot = np.logical_not(p1f)
        p1comp = np.concatenate((p1f, p1fnot), axis=0)

        p2f = np.asarray(phone2.getfeatures()).astype(np.bool)
        p2fnot = np.logical_not(p2f)
        p2comp = np.concatenate((p2f, p2fnot), axis=0)

        return round(spatial.distance.jaccard(p1comp, p2comp),3)

    def simpleMatchingDistance(sefl, p1, p2):
        phone1 = phone(p1)
        phone2 = phone(p2)
        p1f = np.asarray(phone1.getfeatures()).astype(np.bool)
        p2f = np.asarray(phone2.getfeatures()).astype(np.bool)
        
        if p1f.shape != p2f.shape:
            raise ValueError("Shape mismatch: both phones must have the same shape.")
    
        a = np.logical_and(p1f, p2f).sum()
        b_plus_c = np.logical_xor(p1f, p2f).sum()
        d = np.logical_not(np.logical_or(p1f, p2f)).sum()

        return float((b_plus_c / (a + b_plus_c + d)))
    
    def normsimilarity(sefl, p1, p2):
        phone1 = phone(p1)
        phone2 = phone(p2)
        p1f = np.array(phone1.getfeatures())
        p2f = np.array(phone2.getfeatures())
        correct_matches = sum(i > 0 for i in list(p1f & p2f))
        return correct_matches/len(p1f)
