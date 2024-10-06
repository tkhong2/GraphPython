import networkx as nx
#Tạo đồ thị
G = nx.DiGraph()
#Thêm đỉnh
nodes = ['a', 'b','c', 'd', 'e', 'f', 'g','h', 'i']
G.add_nodes_from (nodes)
#Thêm cạnh
edges = [('a', 'b'),('c', 'a'), ('c', 'd'), ('d', 'e'), ('e', 'g'), ('e', 'h'), ('f', 'e'), ('g', 'c'), ('g', 'i'), ('h', 'f')]
G.add_edges_from (edges)
#Tính số đỉnh của đồ thị
n = G.number_of_nodes() #n = len(nodes)
print ("Sổ đỉnh n của đồ thị là: n = ", (n))
#Khởi tạo ma trận kề
adj_matrix = [[0] * n for _ in range(n)]
# Tạo ma trận kề bằng cách duyệt qua các cạnh trong đồ thị
for u_node, v_node in G.edges():
    u_index = nodes.index(u_node)  # Tìm chỉ số của đỉnh u_node
    v_index = nodes.index(v_node)  # Tìm chỉ số của đỉnh v_node
    adj_matrix[u_index][v_index] = 1
    adj_matrix[v_index][u_index] = 1  # Nếu đồ thị vô hướng
# In ma trận kề
print("\nMa trận kề của đồ thị:")
for i, row in enumerate(adj_matrix):
    print(nodes[i], row)

#Biểu diễn bằng danh sách kề
# Khởi tạo danh sách kề trống
adj_list = {node: [] for node in nodes}

# Tạo danh sách kề bằng cách duyệt qua các cạnh trong đồ thị
for u_node, v_node in G.edges():
    adj_list[u_node].append(v_node)
    adj_list[v_node].append(u_node)  # Nếu đồ thị vô hướng

# In danh sách kề
print("\nDanh sách kề của đồ thị:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")