#Biểu diễn ma trận trọng số
# Khởi tạo ma trận trọng số với giá trị ban đầu là vô cực (inf)
import networkx as nx
import numpy as np
G = nx.Graph()
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
edges = [
    ('a','b', 4),
    ('a','c',3),
    ('a','f',5),
    ('b','a',4),
    ('b','e',6),
    ('b','f',2),
    ('c','d',13),
    ('c','f',1),
    ('d','f',3),
    ('d','g',9),
    ('e','f',7),
    ('e','g',2),
    ('f','g',1)
]
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)
n = len(nodes)
INF = float('inf')
weight_matrix = [[INF] * n for _ in range(n)]
# Tạo ánh xạ từ đỉnh sang chỉ số
node_to_index = {node: i for i, node in enumerate(nodes)}
# Đánh dấu trọng số cho các cạnh trong ma trận
for u, v, weight in edges:
    i, j = node_to_index[u], node_to_index[v]
    weight_matrix[i][j] = weight
# Đặt trọng số của cạnh từ một đỉnh tới chính nó là 0
for i in range(n):
    weight_matrix[i][i] = 0
# Hiển thị ma trận trọng số với tên đỉnh
print("Ma trận trọng số:")
for row in enumerate(weight_matrix):
    print(row)  

