import msprime
import numpy as np
import math
import os
import re
import random
import math
import sys
from multiprocessing import Process,Manager
import matplotlib
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import umap
from sklearn.manifold import TSNE


################################################
##RUN SIMULATION FROM SLIM

OUT='LOG_SLIM'
os.system('slim simulation_test11.eid > {}'.format(OUT))

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

###################################################
#open produced vcf file
# vcf=open('mating.vcf','r')


TEST11=open('test11.txt','r')
TEST11.readline()


TRS=[]
FKS=[]
Gen=[]

for line in TEST11:
    line=line.strip().split()
    FKS.append(float(line[0]))
    TRS.append(float(line[1]))
    Gen.append(float(line[2]))


FKS=[x*500 for x in FKS]

plt.figure(figsize=(100, 60))
plt.plot([x for x in Gen], [x for x in FKS], color='blue',linewidth=2)
plt.plot([x for x in Gen], [x for x in TRS], color='red',linewidth=2)
plt.xlabel('Generation')
plt.ylabel('True Sex ratio (red) and Fake Sex ratio (blue)')


plt.show()

