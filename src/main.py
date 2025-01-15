from utils import parse_tsplib
from utils import compute_distance_matrix
from christofides import christofides
from twice_around_tree import twice_around_tree 
from branch_and_bound import bnb_tsp
import time

def main():
    file_path = "../datanew/berlin52.tsp"
    dimension, node_coords, edge_weight_type = parse_tsplib(file_path)
    distance_matrix = compute_distance_matrix(node_coords, edge_weight_type)

    # Executa o algoritmo Twice-Around-the-Tree
    start_time = time.time()
    tatt_route, tatt_cost = twice_around_tree(distance_matrix)
    tatt_time = time.time() - start_time
    print("Dimensão: ", dimension)
    print("TSP Solver - Twice-Around-the-Tree")
    print("------------------------------------------------------------------------")
    print(f"Rota Aproximada (Twice-Around-the-Tree): {tatt_route}")
    print(f"Custo Total Aproximado (Twice-Around-the-Tree): {tatt_cost}")
    print(f"Tempo de execução (Twice-Around-the-Tree): {tatt_time:.4f} segundos")
    print("------------------------------------------------------------------------")

    # Executa o algoritmo de Christofides
    start_time = time.time()
    ch_route, ch_cost = christofides(distance_matrix)
    ch_time = time.time() - start_time
    print("TSP Solver - Christofides")
    print("------------------------------------------------------------------------")
    print(f"Rota Aproximada (Christofides): {ch_route}")
    print(f"Custo Total Aproximado (Christofides): {ch_cost}")
    print(f"Tempo de execução (Christofides): {ch_time:.4f} segundos")
    print("------------------------------------------------------------------------")

    # Executa o algoritmo Branch-and-Bound
    start_time = time.time()
    bnb_route, bnb_cost = bnb_tsp(distance_matrix)
    bnb_time = time.time() - start_time
    print("TSP Solver - Branch-and-Bound")
    print("------------------------------------------------------------------------")
    print(f"Custo Total (Branch-and-Bound): {bnb_cost}")
    print(f"Rota Ótima (Branch-and-Bound): {bnb_route}")
    print(f"Tempo de execução (Branch-and-Bound): {bnb_time:.4f} segundos")
    print("------------------------------------------------------------------------")

if __name__ == "__main__":
    main()