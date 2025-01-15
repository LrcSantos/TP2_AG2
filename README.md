# Trabalho Prático 2: Algoritmos II


# Requisitos

Para executar o programa, é necessário a biblioteca `networkx` instalada.


# Como executar o programa no terminal

## Passo a Passo

1. O arquivo principal do programa é `main.py`, localizado na pasta `src`.

3. Use os argumentos abaixo para executar o programa:

### Argumentos 

- **Opções para escolher qual algoritmo:**
  - `-c`: executar algoritmo Christofides
  - `-t`: executar algoritmo Twice-Around-the-Tree"
  - `-b`: executar algoritmo Branch-and-Bound
  - `-all`: executar todos os algoritmos (default)

Caso não seja passado nenhuma opção de algoritmo, então todos os algoritmos serão executados, equivalente a opção "-all". Pode ser escolhido 1 ou 2 opções de algoritmos, ou seja, é possível rodar um individualmente ou fazer qualquer combinação entre dois parâmetros entre '-c', '-t', '-b', não importando ordem.

### Argumentos Opcionais


### Formato Geral do Comando

```bash
python3 ./src/main.py ./data/teste < opções > 
```

4. Após a execução, os resultados serão printados no terminal e salvos no arquivo `output.txt`.

##  Exemplos
 
 ```bash
python3 ./src/main.py ./data/a280.tsp -c
```

 ```bash
python3 ./src/main.py ./data/fl1400.tsp -t
```

 ```bash
python3 ./src/main.py ./data/fl1400.tsp -t -c
```

 ```bash
python3 ./src/main.py ./data/fl1400.tsp -all
```

 ```bash
python3 ./src/main.py ./data/fl1400.tsp
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
