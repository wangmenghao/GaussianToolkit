import numpy as np
import re
from numpy.lib.function_base import extract
import pandas as pd
from numpy.linalg import norm
import math


'''defines methods for data processing'''
def __init__(self) -> None:
    pass
def dist(A,B):
    return math.sqrt(sum([(a - b)**2 for (a, b) in zip(A,B)]))

def distToOneAtom(atomDF, atom="Ir"):
    coords     = atomDF[["X", "Y", "Z"]]
    atomid     = atomDF[atomDF["Atom"] == "Ir" ].index.tolist()
    centerAtom = atomDF[["X", "Y", "Z"]].iloc[atomid[0]].to_list()

    distdf = []

    extracted = pd.DataFrame()

    for index, data in coords.iterrows():
        d = dist(data.to_list(), centerAtom)
        distdf.append(d)

    atomDF["DistTo"+ atom] = distdf
    extracted = atomDF.sort_values(by="DistTo"+atom).groupby("Atom").first()

    return extracted

def get_charges_by_name(atomDF, atom="N", type="NBO"):

    return atomDF.loc[(atomDF["Atom"] == atom )]["NBO Charge"].item()

    
