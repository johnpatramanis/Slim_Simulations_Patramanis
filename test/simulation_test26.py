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
os.system('slim simulation_test26.eid > {}'.format(OUT))

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


TEST11=open('test26.txt','r')

SIZE=[]
AGE=[]
Gen=[]

for line in TEST11:
    line=line.strip().split()
    SIZE.append(float(line[0]))
    AGE.append(float(line[1]))
    Gen.append(float(line[2]))



plt.figure(figsize=(100, 60))
plt.plot([x for x in Gen], [x for x in SIZE], color='blue',linewidth=0.5)
plt.xlabel('Generation')
plt.ylabel('Pop Size')
plt.show()


plt.figure(figsize=(100, 60))
plt.xlabel('Generation')
plt.ylabel('Avg Age')
plt.plot([x for x in Gen], [x for x in AGE], color='red',linewidth=0.5)

plt.show()

