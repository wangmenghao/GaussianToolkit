# GaussianToolkit
A versatile toolkit to extract DFT calculation data from Gaussian output file. 

# The Molecule class
Defined in Classes.py. Read gaussian log file and adapt data into pandas dataframe Molecule.Atoms .

# The Calculator class
Defined in Classes.py. Contains algorithms for calculation. 
Including:
distToOneAtom(molecule, atomid=#) : calculate the distances of all atoms in molecule to # atom, append to moleucule.Atoms.

To be continued

# Command line example

Put log file in current folder

![image](https://github.com/wangmenghao/GaussianToolkit/blob/main/img/cmdexmple.png)

# Batch example

