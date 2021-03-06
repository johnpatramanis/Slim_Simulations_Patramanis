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
from sklearn.linear_model import LinearRegression
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
    GENERATIONS.append(int(Heterohere[-2]))
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
        GENERATIONS.append(int(Heterohere[-2]))
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
        if y == Start:
            Start=x
        if y == End:
            End=x
    
    print(Start,End)
    
    Heteroz=Heteroz[Start:End]
    Heterozvar=Heterozvar[Start:End]
    POPSIZE=POPSIZE[Start:End]
    GENERATIONS=GENERATIONS[Start:End]
    
    InitSize=POPSIZE[0]
    for j,k in enumerate(POPSIZE):
        if k<=InitSize*0.05:
            Endpoint=j
            break
        else:
            Endpoint=len(POPSIZE)
    
    #################### FOR POPULATION SIZE SLOPE CALCS ##########################################
    X = np.array(POPSIZE[:Endpoint]).reshape((-1, 1))
    Y = np.array(GENERATIONS[:Endpoint])
    Z = np.array(Heteroz[:Endpoint]).reshape((-1, 1))
    
    
    model = LinearRegression()
    model.fit(X, Y)
    r_sq = model.score(X, Y)
    
    LINE_PRED=model.predict(X)
    
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)
    
    
    #################### FOR PI SLOPE CALCS ##########################################
    
    model2 = LinearRegression()
    model2.fit(Z, Y)
    r_sq2 = model2.score(Z, Y)
    
    LINE_PRED2=model2.predict(Z)
    
    print('coefficient of determination:', r_sq2)
    print('intercept:', model2.intercept_)
    print('slope:', model2.coef_)
    
    
    
    
    
    
    
    
    
    plt, axs = plt.subplots(2)

    # plt.ylim(0,max(Heteroz)*1.5)

    # plt.title('π through generations')
    # plt.xlabel('Generation')
    # plt.ylabel('π')


    
    axs[0].plot(GENERATIONS,Heteroz,label='π')
    axs[0].plot(LINE_PRED2,Heteroz[:Endpoint],label='π Slope',color='red')
    axs[0].plot(GENERATIONS,Heterozvar,label='StdDev')
    # axs[0].text(60100,np.median(Heteroz[:Endpoint]),"Slope Coef: {} \n Intersept: {} \n Score: {}".format(model2.coef_[0],model2.intercept_,r_sq2),fontsize=10)
    axs[0].set( ylabel='π and StdDev')
    axs[0].set(title='{}'.format(args.hetero[0]))
    axs[0].legend()
    
    
    axs[1].plot(GENERATIONS,POPSIZE)
    axs[1].plot(LINE_PRED,POPSIZE[:Endpoint],color='red')
    axs[1].text(60100,np.mean(POPSIZE[:Endpoint]),"Slope Coef: {} \n Intersept: {} \n Score: {}".format(model.coef_[0],model.intercept_,r_sq),fontsize=10)
    axs[1].set(xlabel='Generations', ylabel='Population Sizez')
    # plt.show()
    plt.savefig('Zoomed_{}.pdf'.format(args.hetero[0])) 

    # If we want to see pop size as well!
    # plt.scatter(GENERATIONS,POPSIZE,s=10,color='red')
    # plt.plot(GENERATIONS,POPSIZE,color='red')





else:
    plt, axs = plt.subplots(2)

    # plt.ylim(0,max(Heteroz)*1.5)

    # plt.title('π through generations')
    # plt.xlabel('Generation')
    # plt.ylabel('π')


    axs[0].set(title='{}'.format(args.hetero[0]))
    axs[0].plot(GENERATIONS,Heteroz,label='π')
    axs[0].plot(GENERATIONS,Heterozvar,label='StdDev')
    axs[0].set( ylabel='π and StdDev')
    axs[0].legend()

    axs[1].plot(GENERATIONS,POPSIZE)
    axs[1].set(xlabel='Generations', ylabel='Population Size')
    # plt.show()
    plt.savefig('Overall_{}.pdf'.format(args.hetero[0])) 

    # If we want to see pop size as well!
    # plt.scatter(GENERATIONS,POPSIZE,s=10,color='red')
    # plt.plot(GENERATIONS,POPSIZE,color='red')





# plt.show()


