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

parser.add_argument('--zoom',nargs='+',type=str)



args = parser.parse_args()

Hetero_title=args.hetero[0]
Heteroz=[]
Heterozvar=[]
GENERATIONS=[]
POPSIZE=[]

NUMBEROFREPS= len(glob.glob('./{}[0-9]*'.format(args.hetero[0])))
print (NUMBEROFREPS)

for rep in range(0,NUMBEROFREPS):
    Heterohere=[]
    FILE=open(Hetero_title+str(rep),'r')
    print('reading File number {}'.format(rep))
    for line in FILE:
        Heterohere.append(float(line.strip()))
    GENERATIONS.append(Heterohere[-2])
    POPSIZE.append(Heterohere[-1])
    
    Heterohere=Heterohere[:-2] 
    
    Heterozvarhere=np.std(Heterohere)
    Heterozvar.append(Heterozvarhere)
    
    Heterohere=np.mean(Heterohere)
    Heteroz.append(Heterohere)
    FILE.close()

NUMBEROFREPS= len(glob.glob('./{}Bottle_[0-9]*'.format(args.hetero[0])))
print (NUMBEROFREPS)

if NUMBEROFREPS!=0:
    for rep in range(0,NUMBEROFREPS):
        Heterohere=[]
        FILE=open('Hetero_Bottle_'+str(rep),'r')
        print('reading File number {}'.format(rep))
        
        for line in FILE:
            Heterohere.append(float(line.strip()))
        GENERATIONS.append(Heterohere[-2])
        print(Heterohere[-2])
        POPSIZE.append(Heterohere[-1])
        
        Heterohere=Heterohere[:-2] 
        
        Heterozvarhere=np.std(Heterohere)
        Heterozvar.append(Heterozvarhere)
        
        Heterohere=np.mean(Heterohere)
        Heteroz.append(Heterohere)
        
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
        print(x,y)
        if y == Start:
            Start=x
        if y == End:
            End=x
    
    print(Start,End)
    
    Heteroz=Heteroz[Start:End]
    Heterozvar=Heterozvar[Start:End]
    POPSIZE=POPSIZE[Start:End]
    GENERATIONS=GENERATIONS[Start:End]
    
    
    plt, axs = plt.subplots(2)

    # plt.ylim(0,max(Heteroz)*1.5)

    # plt.title('π through generations')
    # plt.xlabel('Generation')
    # plt.ylabel('π')



    axs[0].plot(GENERATIONS,Heteroz,label='π')
    axs[0].plot(GENERATIONS,Heterozvar,label='StdDev')
    axs[0].set( ylabel='π and StdDev')
    axs[0].legend()

    axs[1].plot(GENERATIONS,POPSIZE)
    axs[1].set(xlabel='Generations', ylabel='Population Size')
    # plt.show()
    plt.savefig('line_plot.pdf') 

    # If we want to see pop size as well!
    # plt.scatter(GENERATIONS,POPSIZE,s=10,color='red')
    # plt.plot(GENERATIONS,POPSIZE,color='red')





else:
    plt, axs = plt.subplots(2)

    # plt.ylim(0,max(Heteroz)*1.5)

    # plt.title('π through generations')
    # plt.xlabel('Generation')
    # plt.ylabel('π')



    axs[0].plot(GENERATIONS,Heteroz,label='π')
    axs[0].plot(GENERATIONS,Heterozvar,label='StdDev')
    axs[0].set( ylabel='π and StdDev')
    axs[0].legend()

    axs[1].plot(GENERATIONS,POPSIZE)
    axs[1].set(xlabel='Generations', ylabel='Population Size')
    # plt.show()
    plt.savefig('line_plot.pdf') 

    # If we want to see pop size as well!
    # plt.scatter(GENERATIONS,POPSIZE,s=10,color='red')
    # plt.plot(GENERATIONS,POPSIZE,color='red')





# plt.show()


