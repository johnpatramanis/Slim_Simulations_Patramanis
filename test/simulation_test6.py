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
os.system('slim simulation_test6.eid > {}'.format(OUT))

##################################################
#FUNCTIONS

TEST6=open('test6.txt','r')

Freq1=[]
Freq2=[]
Gen=[]
for line in TEST6:
    line=line.strip().split()
    Freq1.append(float(line[0]))
    Freq2.append(float(line[1]))
    Gen.append(float(line[2]))


plt.figure(figsize=(100, 60))
plt.plot([x for x in Gen], [x for x in Freq1], color='blue',linewidth=2)
plt.plot([x for x in Gen], [x for x in Freq2], color='red',linewidth=2)

plt.show()
