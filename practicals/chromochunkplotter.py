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

#python3 heterozplotter.py --chunk Hetero_ 100 300

#arguments
parser = argparse.ArgumentParser()
parser.add_argument('--chunk',nargs='+',type=list)



args = parser.parse_args()

TAGS=args.chunk
Chunk_title=''.join(TAGS[0])
START=''.join(TAGS[1])
FINISH=''.join(TAGS[2])

print(Chunk_title,START,FINISH)


Heteroz=[]
GENS=[]
for N in range(int(START),int(FINISH)):
    Heterohere=[]
    FILE=open('{}{}'.format(Chunk_title,N),'r')
    for LINE in FILE:
        Heterohere.append(float(LINE))
    GENS.append(Heterohere[-2])
    Heterohere=Heterohere[:-2]
    Heteroz.append(Heterohere)
        
    FILE.close()


MEANS=[]
SDs=[]

for K in range(0,len(Heteroz[0])):
    collector=[]
    for L in range(0,len(Heteroz)):
        collector.append(float(Heteroz[L][K]))
    MEANS.append(np.mean(collector))
    SDs.append(np.std(collector))
        

POSITIONS=[x for x in range(0,len(Heteroz[0]))]


# print(POSITIONS)


plt.figure(figsize=(100, 60))

plt.title('Pi alonng chromosome from Gen {} to {} '.format(int(GENS[0]),int(GENS[-1])))
plt.plot(POSITIONS,MEANS,label='Mean')
plt.plot(POSITIONS,SDs,label='Stand Dev')
plt.xlabel('Kilo Bases - Window')
plt.ylabel('Mean Pi')
plt.legend()
# plt.scatter(GENERATIONS,POPSIZE,s=10,color='red')


plt.show()
# plt.savefig('line_plot.pdf') 

# plt.scatter(GENERATIONS,POPSIZE,s=10,color='red')



