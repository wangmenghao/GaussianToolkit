import numpy as np
import re
import pandas as pd
from scipy.spatial import distance_matrix

class Gaussian_module:
    def __init__(self, file):
        
        self.Atoms = pd.DataFrame()
        self.Distaces = pd.DataFrame()
        self.lines = open(file, 'r').readlines()
        for i in range(0, len(self.lines)):
            if "NAtoms" in self.lines[i]:
                num = self.lines[i].split()[1]
                self.numAtom = int(num)
                break

    def getData(self, phrase="Symbolic Z-matrix:", ident=2):
        #
        #Function to get inline data, mainly atomistic
        #Returns a numpy asarray
        #
        ident=int(ident)
        datalist = []
        for i in range(0, len(self.lines)):
            if phrase in self.lines[i]:
                for i in range(int(i+ident), i+self.numAtom+ident):
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

        Atoms['Atom Name']         = self.getData(phrase="Symbolic Z-matrix:", ident=2)[0]
        coords                     = self.getData(phrase="Standard ori", ident=5)
        Atoms['X Coords']          = pd.to_numeric(coords[3])                                                                                                 
        Atoms['Y Coords']          = pd.to_numeric(coords[4])                                                                                                
        Atoms['Z Coords']          = pd.to_numeric(coords[5]) 
        Atoms['Mulliken Charge']   = pd.to_numeric(self.getData(phrase='Summary of Natural Population Analysis:', ident=6)[2])
        Atoms['NBO Charge']        = pd.to_numeric(self.getData(phrase='Mulliken charges:', ident=2)[2])


        self.Atoms = Atoms