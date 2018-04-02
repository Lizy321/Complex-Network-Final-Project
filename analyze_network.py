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

# np_a2q = DataFrame(list(sub_a2q.edges)).as_matrix()
# np.savetxt('/Users/lizy/Downloads/Q3/Complex_Network/project/a2q_subgraph.txt',np_a2q)
# np_c2a = DataFrame(list(sub_a2q.edges)).as_matrix()
# np.savetxt('/Users/lizy/Downloads/Q3/Complex_Network/project/c2a_subgraph.txt',np_c2a)
# np_c2q = DataFrame(list(sub_a2q.edges)).as_matrix()
# np.savetxt('/Users/lizy/Downloads/Q3/Complex_Network/project/c2q_subgraph.txt',np_c2q)


def df_cen(data,str):
    return DataFrame({'node': list(data.keys()), str: list(data.values())})

# compute the centrality in each layer
def centrality(G):
    time1 = time.time()
    degree = nx.degree_centrality(G)

    df_degree = df_cen(degree,'degree')

    print("Degree computed!")

    time2 = time.time()
    print(time2-time1)

    betweenness = nx.betweenness_centrality(G)
    df_betweenness = df_cen(betweenness, 'betweenness')
    print("Betweenness computed!")

    time3 = time.time()
    print(time3 - time2)

    closeness = nx.closeness_centrality(G)
    df_closeness = df_cen(closeness, 'closeness')
    print("Closeness computed!")

    time4 = time.time()
    print(time4 - time3)

    communicability = nx.communicability(G)
    df_communicability = df_cen(communicability, 'communicatibility')
    print("Communicability computed!")

    time5 = time.time()
    print(time5 - time4)

    centralities = pd.merge(df_degree, df_betweenness, df_closeness, df_communicability, on=['node'], how='outer')

    return centralities

cent_a2q = centrality(sub_a2q)
cent_c2q = centrality(sub_c2q)
cent_c2a = centrality(sub_c2a)

def write_file(data,activity):
    np.savetxt('/Users/lizy/Downloads/Q3/Complex_Network/project/'+ activity +'_centrality.txt',data.as_matrix())

write_file(cent_a2q,'a2q')
write_file(cent_c2q,'c2q')
write_file(cent_c2a,'c2a')

# Correlation between these centralities can be implmented in the following
