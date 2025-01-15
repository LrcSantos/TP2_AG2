import networkx as nx

def twice_around_tree(distance_matrix):
    """
    Implementa o algoritmo Twice-Around-the-Tree para o problema do TSP.
    """
    num_nodes = len(distance_matrix)
    graph = nx.Graph()

    # Construir o grafo a partir da matriz de distâncias
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            graph.add_edge(i, j, weight=distance_matrix[i][j])

    # Construir a Árvore Geradora Mínima (MST)
    mst = nx.minimum_spanning_tree(graph)

    # Seja dfs_nodes a lista de vértices de mst em pré-ordem a partir de root
    dfs_nodes = list(nx.dfs_preorder_nodes(mst, source=0))

    # Adiciona o vértice inicial no final de dfs_nodes para fechar o ciclo
    dfs_nodes.append(dfs_nodes[0])

    # Calcula o custo diretamente da matriz de distâncias
    total_cost = sum(
        distance_matrix[dfs_nodes[i]][dfs_nodes[i + 1]] for i in range(len(dfs_nodes) - 1)
    )

    return dfs_nodes, total_cost