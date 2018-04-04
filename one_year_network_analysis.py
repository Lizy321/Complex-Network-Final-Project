import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import time
from multiprocessing import Pool
import itertools
import networkx as nx
import random


# =======================
    #This is a one-year data process
# =======================
c2a = np.loadtxt('/Users/lizy/Downloads/Q3/Complex_Network/project/c2a_subgraph.txt')
a2q = np.loadtxt('/Users/lizy/Downloads/Q3/Complex_Network/project/a2q_subgraph.txt')
c2q = np.loadtxt('/Users/lizy/Downloads/Q3/Complex_Network/project/c2q_subgraph.txt')

def create_graph(data):
	G = nx.Graph()
	edges = data[:,0:2].copy()
	G.add_edges_from(edges)
	return G

G_c2a = create_graph(c2a)
G_a2q = create_graph(a2q)
G_c2q = create_graph(c2q)

list_of_nodes = random.sample(list(G_c2a.nodes),5000)


def nodes_from_max_network(data):
	return max(nx.connected_component_subgraphs(data.subgraph(list_of_nodes)), key=len).nodes()

def construct_final_graph(c2a,a2q,c2q):
	nodes = list(set(nodes_from_max_network(c2a)) & set(nodes_from_max_network(a2q)) & set(nodes_from_max_network(c2q)))
	g_c2a = c2a.subgraph(nodes)
	g_a2q = a2q.subgraph(nodes)
	g_c2q = c2q.subgraph(nodes)
	return g_c2a,g_a2q,g_c2q


g_c2a, g_a2q, g_c2q = construct_final_graph(G_c2a,G_a2q,G_c2q)

def add_timestamp(sub_a2q,asq_1y):

    np_a2q = DataFrame(list(sub_a2q.edges))
    np_a2q.columns = ['source','destination']
    df_a2q_1y = DataFrame(list(asq_1y))
    df_a2q_1y.columns = ['source','destination','timestamp']
    df_sub_a2q = pd.merge(np_a2q,df_a2q_1y,on = ['source','destination'],how = 'inner')
    np_a2q = df_sub_a2q.as_matrix()
    return np_a2q,df_sub_a2q

np_a2q = add_timestamp(g_a2q,a2q)
#np.savetxt('/Users/lizy/Downloads/Q3/Complex_Network/project/a2q_small_sub.txt',np_a2q,fmt='%d')

np_c2a = add_timestamp(g_a2q,a2q)
#np.savetxt('/User = add_timestamp(g_c2a,c2a)
#np.savetxt('/Users/lizy/Downloads/Q3/Complex_Network/project/c2a_small_sub.txt',np_c2a,fmt='%d')

np_c2q = add_timestamp(g_c2q,c2q)
#np.savetxt('/Users/lizy/Downloads/Q3/Complex_Network/project/c2q_small_sub.txt',np_c2q,fmt='%d')

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
    cent1 = pd.merge(df_degree, df_betweenness,how='left',on=['node'])
    cent2 = pd.merge(cent1, df_closeness, how='left',on=['node'])
    return cent2


cent_a2q = centrality(g_a2q)
cent_c2q = centrality(g_c2q)
cent_c2a = centrality(g_c2a)

def write_file(data,activity):
	np.savetxt('/Users/lizy/Downloads/Q3/Complex_Network/project/'+ activity +'_centrality.txt',data.as_matrix())

write_file(cent_a2q,'a2q')
write_file(cent_c2q,'c2q')
write_file(cent_c2a,'c2a')




# def partitions(nodes, n):
# 	"Partitions the nodes into n subsets"
# 	nodes_iter = iter(nodes)
# 	while True:
# 		partition = tuple(itertools.islice(nodes_iter,n))
# 		if not partition:
# 			return
# 		yield partition
#
# # To begin the parallel computation, we initialize a Pool object with the
# # number of available processors on our hardware. We then partition the
# # network based on the size of the Pool object (the size is equal to the
# # number of available processors).
#
# def btwn_pool(G):
# 	return nx.betweenness_centrality(G)
#
#
# def between_parallel(G, processes = None):
# 	p = Pool(processes=processes)
# 	part_generator = 4*len(p._pool)
# 	node_partitions = list(partitions(G.nodes(), int(len(G)/part_generator)))
# 	num_partitions = len(node_partitions)
#
#     #Next, we pass each processor a copy of the entire network and
#     #compute #the betweenness centrality for each vertex assigned to the
#     #processor.
#
# 	bet_map = p.map(btwn_pool,
# 					zip([G]*num_partitions,
# 						[True]*num_partitions,
# 						[None]*num_partitions,
# 						node_partitions))
#
#     #Finally, we collect the betweenness centrality calculations from each
#     #pool and aggregate them together to compute the overall betweenness
#     #centrality score for each vertex in the network.
#
# 	bt_c = bet_map[0]
# 	for bt in bet_map[1:]:
# 		for n in bt:
# 			bt_c[n] += bt[n]
# 	return bt_c
#
# bt_c = between_parallel(G_c2a,3)
#
# G_c2a.__getitem__()