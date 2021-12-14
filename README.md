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

Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from Classes import Molecule
>>> mol = Molecule('test.log')
>>> mol.buildDataFrame()
>>> mol.Atoms
   Atom Name  X Coords  Y Coords  Z Coords  Mulliken Charge  NBO Charge
0          C  1.045802  3.234213  2.857134         -0.25406   -0.175298
1          O  1.756946  2.054355  2.546388         -0.49552   -0.323492
......

# Batch example
