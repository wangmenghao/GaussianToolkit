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
        extracted = Function.distToOneAtom(mol.Atoms,"Ir")

        pcharge = extracted.loc['P'].NBO
        ncharge = extracted.loc['N'].NBO
        #print(pcharge)
        #ncharge = extracted[(extracted["Atom"] == "N" )]["NBO Charge"].item()
        datalist.append(pcharge)
        datalist.append(ncharge)
#        print(datalist)
        write.writerow(datalist)

    else:
        print("Job "+ f + " is not complete")
        continue

fh.close()
    
