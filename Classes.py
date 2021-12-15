import numpy as np
import re
import pandas as pd
from numpy.linalg import norm
import math


class Molecule:
    def __init__(self, file):
        
        self.Atoms = pd.DataFrame()
        self.Distaces = pd.DataFrame()
        self.lines = open(file, 'r').readlines()
        for i in range(0, len(self.lines)):
            if "NAtoms" in self.lines[i]:
                num = self.lines[i].split()[1]
                self.numAtom = int(num)
                break

    def getData(self, phrase="Symbolic Z-matrix:", indent=2):
        #
        #Function to get inline data, mainly atomistic
        #Returns a numpy asarray
        #
        indent=int(indent)
        datalist = []
        for i in range(len(self.lines), 0):
            if phrase in self.lines[i]:
                for i in range(int(i+indent), i+self.numAtom+indent):
                   datalist.append(self.lines[i].split())

        return np.asarray(datalist)

    def jobComplete(self):
        # function to check if gaussian job was completed
        # label=0 ->  didnt finish
        # label=1 ->  completed
        label = 0
        for i in self.lines:
        
            if "@" in i:
                label = 1
        return label


    def buildDataFrame(self):

        '''Build DataFrame of Molecues'''

        coords = []

        Atoms = pd.DataFrame()

        Atoms['Atom Name']         = self.getData(phrase="Symbolic Z-matrix:", indent=2)[0]
#        coords                     = self.getData(phrase="Standard ori", indent=5)
#        Atoms['X Coords']          = pd.to_numeric(coords[3])                                                                                                 
#        Atoms['Y Coords']          = pd.to_numeric(coords[4])                                                                                                
#        Atoms['Z Coords']          = pd.to_numeric(coords[5]) 
#        Atoms['Mulliken Charge']   = pd.to_numeric(self.getData(phrase='Mulliken Charges:', indent=2)[2])
        Atoms['NBO Charge']        = pd.to_numeric(self.getData(phrase='Summary of Natural Population Analysis:', indent=6)[2])


        self.Atoms = Atoms


class Calculator:

    '''defines methods for data processing'''

    def __init__(self) -> None:
        pass

    def dist(A,B):
        return math.sqrt(sum([(a - b)**2 for (a, b) in zip(A,B)]))

    def distToOneAtom(atomDF, atomid=0):
        coords = atomDF[["X Coords", "Y Coords", "Z Coords"]]
        centerAtom = atomDF[["X Coords", "Y Coords", "Z Coords"]].iloc[atomid]

        for i in atomDF:
            d = self.dist(i, centerAtom)
            