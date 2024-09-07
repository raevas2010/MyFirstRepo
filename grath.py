import networkx as nx
 
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3, 4])
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4), (3, 4)])
 
print(G.nodes)
print(G.edges)
