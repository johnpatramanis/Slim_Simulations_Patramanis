import msprime
import numpy as np
import math
import os, os.path
import glob
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

#python3 heterozplotter.py --hetero Hetero_

#arguments
parser = argparse.ArgumentParser()
parser.add_argument('--hetero',nargs='+',type=str)



args = parser.parse_args()

Hetero_title=args.hetero[0]
Heteroz=[]
GENERATIONS=[]

NUMBEROFREPS= len(glob.glob('./{}*'.format(args.hetero[0])))
print (NUMBEROFREPS)

for rep in range(0,NUMBEROFREPS):
    Heterohere=[]
    FILE=open(Hetero_title+str(rep),'r')
    print('reading File number {}'.format(rep))
    for line in FILE:
        Heterohere.append(float(line.strip()))
    GENERATIONS.append(Heterohere[-1])
    Heterohere=Heterohere[:-1] 
    Heterohere=np.mean(Heterohere)
    Heteroz.append(Heterohere)
    FILE.close()



# print(Heteroz)
# print(GENERATIONS)

REPS=range(0,len(Heteroz))
# colorz=['b' for x in range(0,len(POSITIONS))] 

plt.figure(figsize=(100, 60))

plt.ylim(0,max(Heteroz)*1.5)

plt.title('π through generations')
plt.xlabel('Generation')
plt.ylabel('π')


plt.scatter([x for x in GENERATIONS],[x for x in Heteroz],s=100)
plt.plot([x for x in GENERATIONS],[x for x in Heteroz])

plt.show()


