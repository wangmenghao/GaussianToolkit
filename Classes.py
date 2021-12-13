import numpy as np
import re
import pandas as pd
from numpy.linalg import norm


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
        for i in range(0, len(self.lines)):
            if phrase in self.lines[i]:
                for i in range(int(i+indent), i+self.numAtom+indent):
                   datalist.append(self.lines[i].split())

        return np.asarray(datalist).swapaxes(0,1)

    def jobComplete(self):
        # function to check if gaussian job was completed
        # label=0 ->  didnt finish
        # label=1 ->  completed
        label = 0
        for i in self.lines:
        
            if "@" in line:
                label = 1
        return label


    def buildDataFrame(self):

        coords = []

        Atoms = pd.DataFrame()

        Atoms['Atom Name']         = self.getData(phrase="Symbolic Z-matrix:", indent=2)[0]
        coords                     = self.getData(phrase="Standard ori", indent=5)
        Atoms['X Coords']          = pd.to_numeric(coords[3])                                                                                                 
        Atoms['Y Coords']          = pd.to_numeric(coords[4])                                                                                                
        Atoms['Z Coords']          = pd.to_numeric(coords[5]) 
        Atoms['Mulliken Charge']   = pd.to_numeric(self.getData(phrase='Summary of Natural Population Analysis:', indent=6)[2])
        Atoms['NBO Charge']        = pd.to_numeric(self.getData(phrase='Mulliken charges:', indent=2)[2])


        self.Atoms = Atoms


class Calculator:

    '''defines methods for data processing'''

    def __init__(self) -> None:
        pass

    def distToOneAtom(a,b):
        return norm(a,b)
