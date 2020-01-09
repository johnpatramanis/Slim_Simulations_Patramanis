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
parser.add_argument('--posfile',nargs='+',type=str)
args = parser.parse_args()



FILE=open(args.posfile[0],'r')

POSITIONS=[]

for line in FILE:
    line=line.strip().split()
    POSITIONS.append([float(x) for x in line])


colormap = plt.get_cmap("plasma")
norm = matplotlib.colors.Normalize(vmin=min([x[2] for x in POSITIONS]), vmax=max([x[2] for x in POSITIONS]))
 


colorz=['b' for x in range(0,len(POSITIONS))] 

plt.figure(figsize=(100, 60))
plt.scatter([x[0] for x in POSITIONS],[x[1] for x in POSITIONS],c=colormap(norm([x[2] for x in POSITIONS])),s=100)

plt.show()
# plt.savefig("plot.pdf",bbox_inches='tight')

