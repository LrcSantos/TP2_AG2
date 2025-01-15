import networkx as nx

def christofides(distance_matrix):
    """
    Implementa o algoritmo de Christofides para resolver o problema do TSP.
    """
    num_nodes = len(distance_matrix)
    graph = nx.Graph()

    # Construir o grafo a partir da matriz de distâncias
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            graph.add_edge(i, j, weight=distance_matrix[i][j])

    # Construir a Árvore Geradora Mínima (MST)
    mst = nx.minimum_spanning_tree(graph)

    # Encontrar os nós com grau ímpar na MST
    odd_degree_nodes = [node for node in mst.nodes if mst.degree[node] % 2 == 1]

    # Construir um subgrafo completo dos nós de grau ímpar
    odd_graph = nx.Graph()
    for i in range(len(odd_degree_nodes)):
        for j in range(i + 1, len(odd_degree_nodes)):
            u = odd_degree_nodes[i]
            v = odd_degree_nodes[j]
            odd_graph.add_edge(u, v, weight=distance_matrix[u][v])

    # Encontrar o emparelhamento mínimo perfeito
    min_matching = nx.algorithms.matching.min_weight_matching(odd_graph)

    # Adicionar as arestas do emparelhamento mínimo perfeito à MST
    multigraph = nx.MultiGraph(mst)
    for u, v in min_matching:
        multigraph.add_edge(u, v, weight=distance_matrix[u][v])

    # Encontrar o circuito Euleriano no multigrafo
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))

    # Transformar o circuito Euleriano em uma solução para o TSP (Remover duplicatas)
    visited = set()
    tsp_route = []
    for u, _ in eulerian_circuit:
        if u not in visited:
            tsp_route.append(u)
            visited.add(u)
    tsp_route.append(tsp_route[0])  # Fechar o ciclo

    # Calcular o custo da rota
    total_cost = sum(
        distance_matrix[tsp_route[i]][tsp_route[i + 1]] for i in range(len(tsp_route) - 1)
    )

    return tsp_route, total_cost