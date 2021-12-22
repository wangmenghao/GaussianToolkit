import Classes
import Function
import os, glob, csv

rootdir = '.'

fh = open('charge.csv', 'w+', newline='')
write = csv.writer(fh)
write.writerow(["filename", 'P', 'N'])


Flist = glob.glob("*.log")
for f in Flist:
    datalist = []
    datalist.append(f)
    print(f)
    mol = Classes.Molecule(f)
    if mol.jobComplete() == True:

        mol.buildDataFrame()
        pcharge = Function.get_charges_by_name(mol.Atoms, atom = "P", type="NBO")[1]
        ncharge = Function.get_charges_by_name(mol.Atoms, atom = "N", type="NBO")[1]
        datalist.extend(pcharge)
        datalist.extend(ncharge)
        print(datalist)
        write.writerow(datalist)

    else:
        print("Job "+ f + " is not complete")
        continue

fh.close()
    
