#!/bin/bash/python3

class phone():
    def __init__(self, vowel, consonant):
    self.vowel = vowel
    self.consonant = consonant

    
class similarity():

    def phonesimilarity(self, p1,p2):
        phone1 = self.getfeature(p1)
        phone2 = self.getfeature(p2)
        if(p1==p2):
            return 1;
        else:
            return 0;
    
    def getfeature(self, phone):
        lvowel = ['A', 'E','I','O','U']
        lconsonant = ['X','Y','Z']
        if p in vowel:
            p.vowel=1
        if p in consonant:
            p.consonant=1
        return p
