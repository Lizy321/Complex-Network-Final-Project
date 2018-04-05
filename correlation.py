import scipy as sc
from scipy import stats
import numpy as np
import csv

c2a = np.loadtxt('C:\\Users\\chitra\\Desktop\\TU-Delft\\modeling\\Complex-Network-Final-Project-master\\data\\c2a_small_sub.txt')
a2q = np.loadtxt('C:\\Users\\chitra\\Desktop\\TU-Delft\\modeling\\Complex-Network-Final-Project-master\\data\\a2q_small_sub.txt')
c2q = np.loadtxt('C:\\Users\\chitra\\Desktop\\TU-Delft\\modeling\\Complex-Network-Final-Project-master\\data\\c2q_small_sub.txt')

closeness = np.loadtxt('C:\\Users\\chitra\\Desktop\\TU-Delft\\modeling\\closeness_centrality.txt')

x = closeness[:,0].copy()
y = closeness[:,1].copy()
z = closeness[:,2].copy()

correl1 = sc.stats.pearsonr(x,y)
correl2 = sc.stats.pearsonr(x,z)
correl3 = sc.stats.pearsonr(y,z)
print correl1
print correl2
print correl3

