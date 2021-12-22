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

    def getData(self, phrase="Symbolic Z-matrix:", indent=2, start=0, end=2):
        #
        #Function to get inline data, mainly atomistic
        #Returns a numpy asarray
        #By default, it returns atom name list
        #
        indent=int(indent)
        datalist = []
        for i in range(len(self.lines)-1, 0, -1):
            if phrase in self.lines[i]:
                for i in range(int(i+indent), i+self.numAtom+indent):
                   datalist.extend(self.lines[i][start:end].split())
                break
        return datalist

    def getChargeData(self, phrase="Summary of Natural Population Analysis:", indent=6):
        #
        #Function to get inline data, mainly atomistic
        #Returns a numpy asarray
        #
        indent=int(indent)
        datalist = []
        for i in range(len(self.lines)-1, 0, -1):
            if phrase in self.lines[i]:
                for i in range(int(i+indent), i+self.numAtom+indent):
                   datalist.append(self.lines[i][11:33].split())
                break
        return np.asarray(datalist).swapaxes(0,1)

    def jobComplete(self):
        # function to check if gaussian job was completed
        # label=0 ->  didnt finish
        # label=1 ->  completed
        label = False
        for i in range(len(self.lines)-50, len(self.lines)):
        
            if "@" in self.lines[i]:
                label = True
        return label


    def buildDataFrame(self):

        '''Build DataFrame of Molecues'''

        coords = []

        Atoms = pd.DataFrame()

        Atoms['Atom Name']         = self.getData(phrase="Symbolic Z-matrix:", indent=2, start=0, end=5)
        coords                     = self.getData(phrase="Standard ori", indent=5, start=38, end=70)
        Atoms['X Coords']          = pd.to_numeric(coords[0])                                                                                                 
        Atoms['Y Coords']          = pd.to_numeric(coords[1])                                                                                                
        Atoms['Z Coords']          = pd.to_numeric(coords[2]) 
        Atoms['Mulliken Charge']   = self.getData(phrase='Mulliken charges:',indent=2, start=12, end=22)
        Atoms['NBO Charge']        = self.getData(phrase='Summary of Natural Population Analysis:', indent=6,start=11, end=20)[0]


        self.Atoms = Atoms
            