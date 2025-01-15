# Trabalho Prático 2: Algoritmos II

Esse trabalho apresenta três algoritimos diferentes para o Problema do Caixeiro Viajante, uma solução exata, baseada no algoritimo Branch-and-Bound, e duas soluções aproximadas, o algoritmo Twice-Around-the-Tree e o algoritmo de Christofides. O objetivo foi fazer uma análise entre eles, em relação a suas diferenças entre desempenho, avaliando métricas de tempo, espaço e solução ótima.

# Requisitos

Para executar o programa, é necessário a biblioteca `networkx` instalada.


# Como executar o programa no terminal

## Passo a Passo

1. O arquivo principal do programa é `main.py`, localizado na pasta `src`.

3. Use os argumentos abaixo para executar o programa:

### Argumentos opcionais para escolha de algoritmos

- **Opções:**
  - `-c`: Executar algoritmo Christofides
  - `-t`: Executar algoritmo Twice-Around-the-Tree"
  - `-b`: Executar algoritmo Branch-and-Bound
  - `-all`: Executar todos os algoritmos (default)

Caso não seja passado nenhuma opção de algoritmo, então todos os algoritmos serão executados, equivalente a opção "-all". Pode ser escolhido 1 ou 2 opções de algoritmos, ou seja, é possível rodar um individualmente ou fazer qualquer combinação entre dois parâmetros entre '-c', '-t', '-b', não importando ordem.

### Argumentos opcionais para tempo

- **Opção:**
  - `-timeout=<tempo>`: Define o tempo máximo de execução em segundos para cada algoritmo

Caso não for passado um valor, cada algoritm escolhido tem o tempo máximo de execução de 30min, passado esse tempo ele é abortado e os dados referentes à execução são colocados como NA (não-disponível). 


### Formato Geral do Comando

```bash
python3 ./src/main.py ./data/teste < opções de algoritmos > [tempo] 
```

4. Após a execução, os resultados serão printados no terminal.

##  Exemplos

* Executa o algoritmo de Christofides (timeout default = 30min):
 
 ```bash
python3 ./src/main.py ./data/a280.tsp -c
```

* Executa o algoritmo de Twice-Around-the-Tree (timeout default = 30min):

 ```bash
python3 ./src/main.py ./data/fl1400.tsp -t
```

* Executa os algoritmos de Twice-Around-the-Tree e Christofides (timeout default = 30min para cada):

 ```bash
python3 ./src/main.py ./data/fl1400.tsp -t -c
```

* Executa os algoritmos de Twice-Around-the-Tree, Christofides e Branch-and-Bound (timeout default = 30min para cada):

 ```bash
python3 ./src/main.py ./data/fl1400.tsp -all
```

* Executa os algoritmos de Twice-Around-the-Tree, Christofides e Branch-and-Bound (timeout default = 30min para cada):

 ```bash
python3 ./src/main.py ./data/fl1400.tsp
```

* Executa o algoritmo de Branch-and-Bound com timeout igual a 10 segundos:

 ```bash
python3 ./src/main.py ./data/fl1400.tsp -b -timeout=10
```

* Executa os algoritmos de Twice-Around-the-Tree e Branch-and-Bound com timeout igual a 10 segundos:

 ```bash
python3 ./src/main.py ./data/fl1400.tsp -t -b -timeout=10
```

## Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="#">
        <sub>
          <b><a href="https://github.com/LrcSantos">Lucas Rafael Costa Santos</a></b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="#">
        <sub>
          <b><a href="https://github.com/luccaamp">Lucca Alvarenga de Magalhães Pinto</a></b>
        </sub>
      </a>
    </td>
  </tr>
</table>
