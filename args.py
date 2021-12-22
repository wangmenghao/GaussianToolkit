import os, sys, csv
import glob
import Classes
import Function

print(sys.argv)

rootdir = '.'

filename = sys.argv[1]+".csv"
print(filename)
title = ['filename']
for i in sys.argv[2:]:
    title.append(i)
    title.append(sys.argv[1])
fh = open(filename, 'w+', newline='')
write = csv.writer(fh)
write.writerow(title)

Flist = glob.glob("*.log")
for f in Flist:
    datalist = []
    datalist.append(f)
    print(f)
    mol = Classes.Molecule(f)
    if mol.jobComplete() == True:

        alist = sys.argv[2:]

        print(alist)

        mol.buildDataFrame()

        for i in alist:
            charge = Function.get_charges_by_name(mol.Atoms, atom = i, type=sys.argv[2])
            datalist.extend(charge)
        print(datalist)
        write.writerow(datalist)

    else:
        print("Job "+ f + " is not complete")
        continue

fh.close()
