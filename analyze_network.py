import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import time

#===================================================================================================
#   The goal is to construct maximum connected network with the same nodes in each layer of network
#===================================================================================================

c2a = np.loadtxt('/Users/lizy/Downloads/Q3/Complex_Network/project/c2a_HALF.txt')
a2q = np.loadtxt('/Users/lizy/Downloads/Q3/Complex_Network/project/a2q_HALF.txt')
c2q = np.loadtxt('/Users/lizy/Downloads/Q3/Complex_Network/project/c2q_HALF.txt')

# construct the maximum subgraph in each layer
def max_subgraph(data):
    edges = data[:,0:2].copy()
    G = nx.Graph()
    G.add_edges_from(edges)
    graphs = max(nx.connected_component_subgraphs(G),key=len)
    print("Maximum Connected Network is Constructed!")
    return graphs

G_c2a = max_subgraph(c2a)
G_a2q = max_subgraph(a2q)
G_c2q = max_subgraph(c2q)


# select the common nodes in each layer and construct a subgraph
def construct_subgraph(a2q,c2a,c2q):
    tic = time.time()
    node1 = a2q.nodes()
    node2 = c2a.nodes()
    node3 = c2q.nodes()
    ret = list(set(node1).intersection(set(node2)).intersection(set(node3)))
    toc = time.time()
    print("Subgraph of each layer is constructed!")
    print("time:" + str(toc-tic) + "s")
    return a2q.subgraph(ret), c2a.subgraph(ret),c2q.subgraph(ret)

sub_a2q, sub_c2a, sub_c2q = construct_subgraph(G_a2q,G_c2a,G_c2q)


# compute the centrality in each layer
def centrality(G):

    degree = nx.degree_centrality(G)
    print("Degree computed!")
    betweenness = nx.betweenness_centrality(G)
    print("Betweenness computed!")
    closeness = nx.closeness_centrality(G)
    print("Closeness computed!")
    communicability = nx.communicability(G)
    print("Communicability computed!")
    df = DataFrame({'degree':degree,'betweenness':betweenness,"closeness":closeness,"communicability":communicability})
    return df

cent_a2q = centrality(sub_a2q)
cent_c2q = centrality(sub_c2q)
cent_c2a = centrality(sub_c2a)

# Correlation between these centralities can be implmented in the following 
