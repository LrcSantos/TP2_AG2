import os
import csv
import time
from multiprocessing import Process, Queue
from utils import parse_tsplib, compute_distance_matrix
from christofides import christofides
from twice_around_tree import twice_around_tree
from branch_and_bound import bnb_tsp

# Diretório contendo os arquivos de instâncias
DATA_DIR = "../datanew"
# Nome do arquivo CSV de resultados
RESULTS_FILE = "../results/resultsnew.csv"
# Tempo limite em segundos (30 minutos)
TIME_LIMIT = 30 * 60

# Lista dos algoritmos disponíveis
ALGORITHMS = {
    "Christofides": christofides,
    "Twice-Around-the-Tree": twice_around_tree,
    "Branch-and-Bound": bnb_tsp,
}

def run_algorithm_with_timeout(algorithm_function, distance_matrix, queue):
    """
    Executa o algoritmo e retorna os resultados via Queue.
    """
    try:
        route, cost = algorithm_function(distance_matrix)
        queue.put((route, cost, None))  # Envia os resultados e nenhum erro
    except Exception as e:
        queue.put((None, None, str(e)))  # Envia erro

def run_experiment(instance_file, algorithm_name, algorithm_function):
    """
    Executa um experimento para uma instância e um algoritmo específicos.
    :param instance_file: Caminho para o arquivo da instância (.tsp).
    :param algorithm_name: Nome do algoritmo a ser executado.
    :param algorithm_function: Função do algoritmo a ser executado.
    :return: Dicionário com resultados (tempo, custo, sucesso).
    """
    try:
        # Parse da instância
        dimension, node_coords, edge_weight_type = parse_tsplib(instance_file)
        distance_matrix = compute_distance_matrix(node_coords, edge_weight_type)

        # Executa o algoritmo com limite de tempo
        queue = Queue()
        process = Process(target=run_algorithm_with_timeout, args=(algorithm_function, distance_matrix, queue))
        start_time = time.time()
        process.start()
        process.join(TIME_LIMIT)  # Aguarda até o limite de tempo

        if process.is_alive():
            process.terminate()
            process.join()
            return {
                "Algorithm": algorithm_name,
                "Time(s)": None,
                "Cost": None,
                "Success": False,
                "Error": f"Exceeded time limit of {TIME_LIMIT / 60} minutes",
                "Dimension": dimension,
            }

        elapsed_time = time.time() - start_time
        route, cost, error = queue.get()

        if error:
            return {
                "Algorithm": algorithm_name,
                "Time(s)": None,
                "Cost": None,
                "Success": False,
                "Error": error,
                "Dimension": dimension,
            }

        return {
            "Algorithm": algorithm_name,
            "Time(s)": round(elapsed_time, 4),
            "Cost": cost,
            "Success": True,
            "Dimension": dimension,
        }
    except Exception as e:
        # Resultado em caso de erro
        return {
            "Algorithm": algorithm_name,
            "Time(s)": None,
            "Cost": None,
            "Success": False,
            "Error": str(e),
            "Dimension": None,
        }

def main():
    # Lista todos os arquivos .tsp no diretório de instâncias
    instances = [f for f in os.listdir(DATA_DIR) if f.endswith(".tsp")]

    # Abre o arquivo CSV para escrita
    with open(RESULTS_FILE, mode="w", newline="") as csvfile:
        fieldnames = ["Instance", "Algorithm", "Time(s)", "Cost", "Success", "Error", "Dimension"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Executa experimentos para cada instância e algoritmo
        for instance in instances:
            instance_path = os.path.join(DATA_DIR, instance)
            print(f"Processing instance: {instance}")

            for algorithm_name, algorithm_function in ALGORITHMS.items():
                print(f"  Running algorithm: {algorithm_name}")
                result = run_experiment(instance_path, algorithm_name, algorithm_function)
                result["Instance"] = instance
                writer.writerow(result)

if __name__ == "__main__":
    main()