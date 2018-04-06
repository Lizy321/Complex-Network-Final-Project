import scipy as sc
from scipy import stats
import numpy as np
import csv
import time

c2a = np.loadtxt('C:\\Users\\chitra\\Desktop\\TU-Delft\\modeling\\Complex-Network-Final-Project-master\\data\\c2a_small_sub.txt')
a2q = np.loadtxt('C:\\Users\\chitra\\Desktop\\TU-Delft\\modeling\\Complex-Network-Final-Project-master\\data\\a2q_small_sub.txt')
c2q = np.loadtxt('C:\\Users\\chitra\\Desktop\\TU-Delft\\modeling\\Complex-Network-Final-Project-master\\data\\c2q_small_sub.txt')

centrality = np.loadtxt('C:\\Users\\chitra\\Desktop\\TU-Delft\\modeling\\centrality.txt')

#clustering centrality
clustering1 = centrality[:,0].copy()
clustering2 = centrality[:,6].copy()
clustering3 = centrality[:,12].copy()

#eigenvector centrality
eigen1 = centrality[:,1].copy()
eigen2 = centrality[:,7].copy()
eigen3 = centrality[:,13].copy()

#pagerank centrality
page1 = centrality[:,2].copy()
page2 = centrality[:,8].copy()
page3 = centrality[:,14].copy()

#closeness centrality
close1 = centrality[:,3].copy()
close2 = centrality[:,9].copy()
close3 = centrality[:,15].copy()

#harmonic centrality
har1 = centrality[:,4].copy()
har2 = centrality[:,10].copy()
har3 = centrality[:,16].copy()

#betweeness centrality
between1 = centrality[:,5].copy()
between2 = centrality[:,11].copy()
between3 = centrality[:,17].copy()



clus1 = sc.stats.pearsonr(clustering1,clustering2)
clus2 = sc.stats.pearsonr(clustering2,clustering3)
clus3 = sc.stats.pearsonr(clustering3,clustering1)


eig1 = sc.stats.pearsonr(eigen1,eigen2)
eig2 = sc.stats.pearsonr(eigen2,eigen3)
eig3 = sc.stats.pearsonr(eigen3,eigen1)



pg1 = sc.stats.pearsonr(page1,page2)
pg2 = sc.stats.pearsonr(page2,page3)
pg3 = sc.stats.pearsonr(page3,page1)


cl1 = sc.stats.pearsonr(close1,close2)
cl2 = sc.stats.pearsonr(close2,close3)
cl3 = sc.stats.pearsonr(close3,close1)


hr1 = sc.stats.pearsonr(har1,har2)
hr2 = sc.stats.pearsonr(har2,har3)
hr3 = sc.stats.pearsonr(har3,har1)


bt1 = sc.stats.pearsonr(between1,between2)
bt2 = sc.stats.pearsonr(between2,between3)
bt3 = sc.stats.pearsonr(between3,between1)


print clustering1
print clustering2
print clustering3
time.sleep(5)

print eigen1
print eigen2
print eigen3

print page1
print page2
print page3

print close1
print close2
print close3

print har1
print har2
print har3

print between1
print between2
print between3


