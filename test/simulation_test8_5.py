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
os.system('slim simulation_test8_5.eid > {}'.format(OUT))

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
    #open produced vcf file
def pca_vcf(vcffile,mutationfile):
    vcf=open(vcffile,'r')
    mutations=open(mutationfile,'r')
    MUT=[]
    for line in mutations:
        line=line.strip().split()
        MUT.append(line)
        
    colorz=[]
    for x in MUT[0]:
        if x == '0':
            colorz.append('b')
        if x == '1':
            colorz.append('g')    
        if x == '2':
            colorz.append('r')    
            
            
    #bypass first line of output , that are not vcf
    runner=1
    counter=0
    while runner:
        line=vcf.readline().strip().split()
        counter+=1
        if len(line)!=0:
            if line[0] == '#CHROM':
                break
        if counter>=100000000:
            print('took too long, something went wrong or too many SNPs')
            break

    #first line of genotypes
    firstline=vcf.readline().strip().split()
    firstgenotypes=firstline[9:]
    genotypes=[[translate_to_int(x)] for x in firstgenotypes]



    for line in vcf:
        line=line.strip().split()
        tempgenotypes=line[9:]
        for ind in range(0,len(tempgenotypes)):
            genotypes[ind].append(translate_to_int(tempgenotypes[ind]))
       
     
    X = np.asarray(genotypes)   
    print(X.shape) 

    ###################################################################

    pca = PCA(n_components=2).fit_transform(X)

    plt.figure(figsize=(100, 60))
    plt.scatter([x[0] for x in pca],[x[1] for x in pca],c=colorz)

    plt.show()
    return(X)


pca_vcf('mating1.vcf','mating1.txt')
pca_vcf('mating2.vcf','mating2.txt')
pca_vcf('mating3.vcf','mating3.txt')