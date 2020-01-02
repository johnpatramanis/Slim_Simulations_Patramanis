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
os.system('slim simulation_test16.eid > {}'.format(OUT))

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


# TEST14=open('diversity.txt','r')

# DIV=[]
# Gen=[]
# NUM=[]

# TEST12.readline()

# for line in TEST14:
    # line=line.strip().split()
    # DIV.append(float(line[0]))
    # Gen.append(float(line[1]))





# plt.figure(figsize=(100, 60))
# plt.plot([x for x in Gen], [x for x in DIV], color='blue',linewidth=2)
# plt.xlabel('Generation')
# plt.ylabel('Mean Heterozigosity of Population')


# plt.show()


# plt.figure(figsize=(100, 60))

# plt.plot([x for x in Gen], [x for x in NUM], color='red',linewidth=2)
# plt.xlabel('Generation')
# plt.ylabel('Number of m5 mutations in Population')


# plt.show()
