import Classes
import Function
import os, glob, csv

rootdir = '.'

fh = open('charge.csv', 'w+', newline='')
write = csv.writer(fh)
write.writerow(["filename", 'atom1', 'charge', 'atom2', 'charge'])


Flist = glob.glob("*.log")
for f in Flist:
    datalist = []
    datalist.append(f)
    print(f)
    mol = Classes.Molecule(f)
    if mol.jobComplete() == True:

        mol.buildDataFrame()
        pcharge = Function.get_charges(mol.Atoms, atom = "P")
        ncharge = Function.get_charges(mol.Atoms, atom = "N")
        print(pcharge)
        print(ncharge)
        datalist.extend(pcharge)
        datalist.extend(ncharge)
        write.writerow(datalist)

    else:
        print("Job "+ f + " is not complete")
        continue

fh.close()
    
