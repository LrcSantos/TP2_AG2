# Trabalho Prático 2: Algoritmos II


# Requisitos

Para executar o programa, é necessário a biblioteca `networkx` instalada.


# Como executar o programa no terminal

## Passo a Passo

1. O arquivo principal do programa é `main.py`, localizado na pasta `src`.

3. Use os argumentos abaixo para executar o programa:

### Argumentos Obrigatórios

- **Opções para escolher qual algoritmo:**
  - `-c`: executar algoritmo christofides
  - `-t`: executar algoritmo twice_around_tree
  - `-b`: executar algoritmo branch_and_bound
  - `-all`: executar todos os algoritmos

### Argumentos Opcionais


### Formato Geral do Comando

```bash
python3 ./src/main.py ./data/teste -opcao 
```

4. Após a execução, o programa:
  - Os resultados serão printados no terminal e salvos no arquivo `output.txt`.

##  Exemplos
 
 ```bash
python3 ./src/main.py ./data/a280.tsp -c
```

 ```bash
python3 ./src/main.py ./data/fl1400.tsp -t
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
