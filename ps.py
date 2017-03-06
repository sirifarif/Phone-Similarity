#!/bin/bash/python3

from scipy import spatial

class phone:
    def __init__(self, phone):
        # 
        VOWELS = ['A', 'E','I','O','U', 'N']
        CONSONANTAL = ['X','Y','Z']
        #APPROXIMANT = []
        #SONORANT = []
        VOICED = ['A' ,'Z', 'U', 'N']
        #CONSTRGL = []
        #SPREADGL = []
        
        #MANNER
        NASAL = ['N', 'M']
        #CONTINUANT = []
        #STRIDENT = []
        #DISTRIBUTED = []
        #LATERAL = []

        
        self.features = [0, 0, 0, 0]

        if phone in VOWELS:
            self.features[0] = 1
        if phone in CONSONANTAL:
            self.features[1] = 1
        if phone in VOICED:
            self.features[2] = 1
        if phone in NASAL:
            self.features[3] = 1    
    def getfeatures(self):
        return self.features
    
    def setfeature(self, index):
        self.features[index] = 1

    def unsetfeature(self, index):
        self.features[index] = 0

class similarity:

    def cosinesimilarity(self, p1,p2):
        phone1 = phone(p1)
        phone2 = phone(p2)
        p1f = phone1.getfeatures()
        p2f = phone2.getfeatures()
        print("features {} {}".format(p1f, p2f))
        return 1 - spatial.distance.cosine(p1f, p2f)
