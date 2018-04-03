import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import time

# =======================
    #This is a one-year data process
# =======================
c2a = np.loadtxt('/Users/lizy/Downloads/Q3/Complex_Network/project/csa_1y.txt')
a2q = np.loadtxt('/Users/lizy/Downloads/Q3/Complex_Network/project/asq_1y.txt')
c2q = np.loadtxt('/Users/lizy/Downloads/Q3/Complex_Network/project/csq_1y.txt')



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