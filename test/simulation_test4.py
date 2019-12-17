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
os.system('slim simulation_test4.eid > {}'.format(OUT))

sweepfile1=open('sweep1.txt','r')
sweepfile2=open('sweep2.txt','r')
fitnessfile=open('fitness.txt','r')


SWEEP1=[]
GENS=[]
SWEEP2=[]
FITNESS1=[]
FITNESS2=[]


counter=0
for line in sweepfile1:
    line=line.strip().split()
    SWEEP1.append(float(line[0]))
    GENS.append(float(line[1]))
    counter+=1
    if counter>=1000:
        break
    
    
    
    
counter=0    
for line in sweepfile2:
    line=line.strip().split()
    SWEEP2.append(float(line[0]))
    counter+=1
    if counter>=1000:
        break


    
 

counter=0 
for line in fitnessfile:
    line=line.strip().split()
    FITNESS1.append(float(line[0]))
    FITNESS2.append(float(line[1]))
    counter+=1
    if counter>=1000:
        break
 

 
print(SWEEP1,SWEEP2,GENS,FITNESS1)

plt.figure(figsize=(100, 60))
plt.plot([x for x in GENS], [x for x in SWEEP1], color='green',linewidth=2)
plt.plot([x for x in GENS], [x for x in SWEEP2], color='red',linewidth=2)

plt.show()


plt.figure(figsize=(100, 60))
plt.plot([x for x in GENS], [x for x in FITNESS1], color='green',linewidth=2)
plt.plot([x for x in GENS], [x for x in FITNESS2], color='red',linewidth=2)

plt.show()


sweepfile1.close()
sweepfile2.close()
fitnessfile.close()

os.system('rm -rf {} '.format(sweepfile1))
os.system('rm -rf {} '.format(sweepfile2))
os.system('rm -rf {} '.format(fitnessfile))
