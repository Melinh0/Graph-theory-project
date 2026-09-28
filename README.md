# TrabalhoGrafos

Projeto da disciplina de Grafos com implementações das estruturas de **grafo** e **dígrafo** e dos principais algoritmos de traversal e caminho mínimo, além de um script que aplica esses algoritmos em um grafo real (dataset DIMACS).

## O que o projeto contém

| Arquivo | Descrição |
| --- | --- |
| `graph.py` | Classe `Graph`: grafo não direcionado (com ou sem pesos). |
| `digraph.py` | Classe `Digraph`: grafo direcionado (com ou sem pesos), com graus de entrada e saída. |
| `main.py` | Script de demonstração: cria um pequeno grafo, executa todos os algoritmos e depois processa o dataset `USA-road-d.NY`. |
| `USA-road-d.NY/USA-road-d.NY.gr` | Instância de grafo do *9th DIMACS Implementation Challenge* (TIGER/Line graph de Nova York): 264.346 vértices e 733.846 arcos. |
| `relatorio_avaliacao2.pdf` | Relatório da avaliação. |

### Algoritmos implementados

* `bfs(v)` — busca em largura (distâncias e predecessores)
* `dfs(v)` — busca em profundidade (predecessores e tempos de início/término)
* `bf(v)` — Bellman-Ford (distâncias mínimas com pesos)
* `djikstra(v)` — Dijkstra (distâncias mínimas com pesos não negativos)

### Operações de consulta

`n()`, `m()`, `viz(v)`, `d(v)`, `w(u, v)`, `mind()`, `maxd()` — número de vértices, número de arestas, vizinhos, grau, peso da aresta, menor e maior grau.

## Requisitos

* **Python 3.8 ou superior**
* O projeto usa apenas a biblioteca padrão (`heapq`, `sys`, `os`) — **não é necessário instalar nenhuma dependência**.

## Como executar

1. Entre na pasta do projeto (após clonar o repositório).

2. Rode o script principal:

   ```bash
   python main.py
   ```

   Em alguns sistemas, use `python3 main.py`.

O caminho do dataset é resolvido de forma automática em relação à localização de `main.py`, então o script funciona em qualquer máquina sem ajustes.

## O que a saída mostra

`main.py` é dividido em duas partes:

1. **Grafo de exemplo** — cria um grafo ponderado com 4 vértices e 5 arestas e imprime o resultado de cada consulta e de cada algoritmo (BFS, DFS, Bellman-Ford e Dijkstra) a partir do vértice `1`.
2. **Análise do dataset `USA-road-d.NY`** — responde às questões da avaliação:
   * `a)` valor de `G.mind()` (menor grau)
   * `b)` valor de `G.maxd()` (maior grau)
   * `c)` um caminho com 10 ou mais arestas
   * `d)` um ciclo com 5 ou mais arestas
   * `e)` o vértice mais distante de `129` e a distância até ele

> Observação: o processamento do dataset lê um arquivo com mais de 700 mil linhas e executa Dijkstra sobre 264 mil vértices, então os itens `c)`, `d)` e `e)` podem levar alguns segundos.

## Formato do arquivo `.gr`

Os arquivos seguem o padrão DIMACS:

```
c comentário
p sp <número de vértices> <número de arcos>
a <origem> <destino> <peso>
```

## Licença

Veja o arquivo [LICENSE](LICENSE).
