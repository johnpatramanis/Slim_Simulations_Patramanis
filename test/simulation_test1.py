import msprime
import numpy as np
import math
import os
import re
import random
import sys
from multiprocessing import Process,Manager
import matplotlib
from matplotlib import pyplot as plt
# matplotlib.use('Agg') 
from sklearn.decomposition import PCA



################################################
##RUN SIMULATION FROM SLIM

OUT='LOG_SLIM'
os.system('slim simulation_test1.eid > {}'.format(OUT))

###################################################
#FUNCTIONS
def translate_to_int(n):
    n=str(n)
    count=n.count('0')
    if count==0:
        k=2
    if count==1:
        k=1
    if count==2:
        k=0
    return k

###################################################
#open produced vcf file
vcf=open(OUT,'r')

#bypass first line of output , that are not vcf
runner=1
counter=0
while runner:
    line=vcf.readline().strip().split()
    counter+=1
    if len(line)!=0:
        if line[0] == '#CHROM':
            break
    if counter>=100000000:
        print('took too long, something went wrong or too many SNPs')
        break

#first line of genotypes
firstline=vcf.readline().strip().split()
firstgenotypes=firstline[9:]
genotypes=[[translate_to_int(x)] for x in firstgenotypes]



for line in vcf:
    line=line.strip().split()
    tempgenotypes=line[9:]
    for ind in range(0,len(tempgenotypes)):
        genotypes[ind].append(translate_to_int(tempgenotypes[ind]))
   
   
print(genotypes)    
    
X = np.asarray(genotypes)    
pca = PCA(n_components=2).fit_transform(X)



print(len(pca))
plt.figure(figsize=(100, 60))
plt.scatter([x[0] for x in pca],[x[1] for x in pca])

plt.show()


