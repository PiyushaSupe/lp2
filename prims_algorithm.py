import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(graph, start_node):
    visited = set([start_node])
    edges = [
        (data['weight'], start_node, to)
        for to, data in graph[start_node].items()
    ]
    mst = nx.Graph()
    while edges:
        edges.sort()
        weight, frm, to = edges.pop(0)
        if to not in visited:
            visited.add(to)
            mst.add_edge(frm, to, weight=weight)
            for next_to, data in graph[to].items():
                if next_to not in visited:
                    edges.append((data['weight'], to, next_to))
    return mst

def get_user_input():
    G = nx.Graph()
    n = int(input("Enter number of nodes: "))
    e = int(input("Enter number of edges: "))
    print("Enter edges in format: node1 node2 weight")
    for _ in range(e):
        u, v, w = input().split()
        G.add_edge(u, v, weight=int(w))
    return G

def draw_graphs(original, mst):
    pos = nx.spring_layout(original)
    plt.figure(figsize=(12, 6))

    # Original Graph
    plt.subplot(121)
    nx.draw(original, pos, with_labels=True, node_color='skyblue', edge_color='gray')
    edge_labels = nx.get_edge_attributes(original, 'weight')
    nx.draw_networkx_edge_labels(original, pos, edge_labels=edge_labels)
    plt.title("Original Graph")

    # MST Graph
    plt.subplot(122)
    nx.draw(mst, pos, with_labels=True, node_color='lightgreen', edge_color='red')
    mst_edge_labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=mst_edge_labels)
    plt.title("Minimum Spanning Tree (Prim's Algorithm)")

    plt.show()

if __name__ == "__main__":
    G = get_user_input()
    start_node = list(G.nodes())[0]
    mst = prim_mst(G, start_node)
    draw_graphs(G, mst)
