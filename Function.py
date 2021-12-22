import numpy as np
import re
import pandas as pd
from numpy.linalg import norm
import math


'''defines methods for data processing'''
def __init__(self) -> None:
    pass
def dist(A,B):
    return math.sqrt(sum([(a - b)**2 for (a, b) in zip(A,B)]))

def distToOneAtom(atomDF, atom="Ir"):
    coords     = atomDF[["X Coords", "Y Coords", "Z Coords"]]
    atomid     = atomDF[atomDF["Atom Name"] == "Ir" ].index.tolist()
    centerAtom = atomDF[["X Coords", "Y Coords", "Z Coords"]].iloc[atomid[0]].to_list()

    distdf = []

    for index, data in coords.iterrows():
        print(data.to_list())
        d = dist(data.to_list(), centerAtom)
        print(d)
        distdf.append(d)

    atomDF["Distance to "+ atom + str(atomid)] = distdf

def get_charges_by_name(atomDF, atom="N", type="NBO"):

    return [atom, atomDF[atomDF["Atom Name"] == atom][type+" Charge"].values]

    
