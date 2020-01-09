import msprime
import numpy as np
import math
import os
import re
import random
import math
import sys
import argparse
from multiprocessing import Process,Manager
import matplotlib
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import umap
from sklearn.manifold import TSNE


#arguments
parser = argparse.ArgumentParser()
parser.add_argument('--vcfile',nargs='+',type=str)
args = parser.parse_args()



##################################################
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






vcf=open( args.vcfile[0],'r')


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


firstline=vcf.readline().strip().split()
firstgenotypes=firstline[9:]
genotypes=[[translate_to_int(x)] for x in firstgenotypes]



for line in vcf:
    line=line.strip().split()
    tempgenotypes=line[9:]
    for ind in range(0,len(tempgenotypes)):
        genotypes[ind].append(translate_to_int(tempgenotypes[ind]))
   
 
X = np.asarray(genotypes)   
print(X.shape) 

colorz=['g' for x in range(0,250)]  + ['r' for x in range(0,250)] + ['b' for x in range(0,250)]
pca = PCA(n_components=2).fit_transform(X)

plt.figure(figsize=(100, 60))
plt.scatter([x[0] for x in pca],[x[1] for x in pca],c=colorz,s=100)

# plt.pause(0.05)
# plt.show()



plt.savefig("plot.pdf",bbox_inches='tight')

