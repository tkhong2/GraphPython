import matplotlib.pyplot as plt
import networkx as nx
G = nx.DiGraph()
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
G.add_nodes_from(nodes)
edges = [('a','b'),('a','c'),('a','e'),('b','f'),('c','d'),('c','f'),('c','g'),('d','b'),('d','h'),('d','e')
                  ,('e','f'),('f','h'),('g','e'),('g','h')]
G.add_edges_from(edges)
n = G.number_of_nodes()
print(f"Ma trận: {n}")
adj_matrix = [[0] * n for _ in range(n)]
for u_node, v_node in G.edges():
    u_index = nodes.index(u_node)
    v_index = nodes.index(v_node)
    adj_matrix[u_index][v_index] = 1
    adj_matrix[v_index][u_index] = 1
print('Ma trận kề của đồ thị:')
for i, row in enumerate(adj_matrix):
    print(nodes[i],row)

adj_list = {node:[] for node in nodes}

for u_node, v_node in G.edges():
    adj_list[u_node].append(v_node)
    adj_list[v_node].append(u_node)

print('Danh sách liên kết của đồ thị:')

for node, neighbors in adj_list.items():
    print(f'{node}: {neighbors}')

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=3)
nx.draw_networkx_labels(G, pos, font_size=20)
plt.show()

