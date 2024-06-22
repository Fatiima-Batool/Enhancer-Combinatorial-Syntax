# code to identify CRMs with specific heterotypic modules
import re
fr=open("chr1.txt","r")
f=fr.read().replace("\t","@").replace("\n","@")
#k=re.split(r'[ \t]', f)
ff=f.split("@")
#print(ff)
for line in ff:
    #print(line)
    if "GATA3, FOXP2, HES5"  in line:
        j=ff.index(line)
        #print(j-1)
        k=j-1

        print(ff[k])
'''i=0
while i < len(ff):
      #print(ff[i])
      if "GATA3, FOXP2, HES5"  in ff:
        print(i)'''
