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
os.system('slim simulation_test18.eid > {}'.format(OUT))

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


TEST18=open('mutations.txt','r')



MUTS=TEST18.readline().strip().split()
MUTS=[int(x) for x in MUTS ]

print(MUTS)

FIRST=len([x for x in MUTS if x<20000])
SECOND=len([x for x in MUTS if x<40000 and x>20000])
THIRD=len([x for x in MUTS if x<60000 and x>40000])
FOURTH=len([x for x in MUTS if x<80000 and x>60000])
FIFTH=len([x for x in MUTS if x>80000])

CHUNKS=[FIRST,SECOND,THIRD,FOURTH,FIFTH]
CHUNKNAMES=['FIRST','SECOND','THIRD','FOURTH','FIFTH']
plt.figure(figsize=(100, 60))
plt.bar(CHUNKNAMES,CHUNKS)
plt.xlabel('20 kb Chunks, each with a different mutation rate')
plt.ylabel('Number of Mutations occuring within the Chunk')


plt.show()


# plt.figure(figsize=(100, 60))

# plt.plot([x for x in Gen], [x for x in NUM], color='red',linewidth=2)
# plt.xlabel('Generation')
# plt.ylabel('Number of m5 mutations in Population')


# plt.show()
