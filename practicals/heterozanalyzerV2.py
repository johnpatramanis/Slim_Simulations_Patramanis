import msprime
import numpy as np
import math
import os, os.path
import glob
import re
import random
import math
import sys
import statsmodels.api as sm 
import argparse
from multiprocessing import Process,Manager
import matplotlib
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import umap
from sklearn.linear_model import LinearRegression
from sklearn.manifold import TSNE


#python3 heterozplotter.py --hetero Hetero_

#arguments
parser = argparse.ArgumentParser()
parser.add_argument('--hetero',nargs='+',type=str)

parser.add_argument('--zoom',nargs='+',type=str)



args = parser.parse_args()

Hetero_title=args.hetero[0]




FILE=open(Hetero_title,'r')
Heteromean=[]
Heterovar=[]
GENERATIONS=[]
POPSIZE=[]

for line in FILE:
    line=line.strip().split()
    Heteromean.append(float(line[0]))
    Heterovar.append(float(line[1]))
    GENERATIONS.append(float(line[2]))
    POPSIZE.append(float(line[3]))

FILE.close()



# print(Heteroz)
# print(GENERATIONS)


# colorz=['b' for x in range(0,len(POSITIONS))] 

# POPSIZE=[(x* 10**(-8)) for x in POPSIZE]


if args.zoom:
    
    
    Start=int(args.zoom[0])
    End=int(args.zoom[1])
    print(Start,End)
    
    for x,y in enumerate(GENERATIONS):
        if y == Start:
            Start=x
        if y == End:
            End=x
    
    
    Heteromean=Heteromean[Start:End]
    Heterovar=Heterovar[Start:End]
    POPSIZE=POPSIZE[Start:End]
    GENERATIONS=GENERATIONS[Start:End]
    
    InitSize=POPSIZE[0]
    for j,k in enumerate(POPSIZE):
        if k<=InitSize*0.05:
            Endpoint=j+100
            break
        else:
            Endpoint=len(POPSIZE)
    
    HeteromeanZoomed=Heteromean
    HeterovarZoomed=Heterovar
    POPSIZEZoomed=POPSIZE
    GENERATIONSZoomed=GENERATIONS
    
    Heteromean=Heteromean[:Endpoint]
    Heterovar=Heterovar[:Endpoint]
    POPSIZE=POPSIZE[:Endpoint]
    GENERATIONS=GENERATIONS[:Endpoint]
    
    
    
    lowess = sm.nonparametric.lowess
    
    X = np.array(Heteromean) ##.reshape((-1, 1))
    X2= np.array(Heterovar)
    Y = np.array(GENERATIONS)
    
    Z = lowess(X, Y , frac=0.2,it=0)
    W = lowess(X2, Y , frac=0.2,it=0)
    
    
    plt, axs = plt.subplots(2)
    axs[0].plot(GENERATIONSZoomed,HeteromeanZoomed,label='π')
    axs[0].plot(GENERATIONSZoomed,HeterovarZoomed,label='StdDev')
    # axs[0].plot([ x[0] for x in Z ],[ x[1] for x in Z ],color='red')
    # axs[0].plot([ x[0] for x in W ],[ x[1] for x in W ],color='purple')
    # axs[0].scatter(np.mean(Y),mean2,color='red',s=20)
    
    # axs[0].plot(LINE_PRED3,Heterozvar[BEGIN:Endpoint],color='purple')
    # axs[0].scatter(np.mean(Y),mean3,color='purple',s=20)
            


    axs[0].set( ylabel='π and StdDev')
    axs[0].set( title='{}'.format(args.hetero[0]))
    axs[0].legend()        
           
    axs[1].plot(GENERATIONSZoomed,POPSIZEZoomed)
    axs[1].set(xlabel='Generations', ylabel='Population Sizez')
    # plt.show()
    plt.savefig('Binned_{}.pdf'.format(Hetero_title)) 
    
    # If we want to see pop size as well!
    # plt.scatter(GENERATIONS,POPSIZE,s=10,color='red')
    # plt.plot(GENERATIONS,POPSIZE,color='red')





else:
    plt, axs = plt.subplots(2)

    # plt.ylim(0,max(Heteroz)*1.5)

    # plt.title('π through generations')
    # plt.xlabel('Generation')
    # plt.ylabel('π')


    axs[0].set( title='{}'.format(args.hetero[0]))
    axs[0].plot(GENERATIONS,Heteromean,label='π')
    axs[0].plot(GENERATIONS,Heterovar,label='StdDev')
    axs[0].set( ylabel='π and StdDev')
    axs[0].legend()
    
    
    axs[1].plot(GENERATIONS,POPSIZE)
    axs[1].set(xlabel='Generations', ylabel='Population Size')
    # plt.show()
    plt.savefig('Overal_{}.pdf'.format(Hetero_title)) 

    # If we want to see pop size as well!
    # plt.scatter(GENERATIONS,POPSIZE,s=10,color='red')
    # plt.plot(GENERATIONS,POPSIZE,color='red')





# plt.show()


