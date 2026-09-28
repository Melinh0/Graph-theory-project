import os

from graph import Graph
from digraph import Digraph

g = Graph(weighted=True)

g.add_edge(1, 2, 4)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 2)
g.add_edge(2, 4, 5)
g.add_edge(3, 4, 8)

print(f"Número de nós: {g.n()}")
print(f"Número de arestas: {g.m()}")
print(f"Vizinhos de 2: {g.viz(2)}")
print(f"Grau de 2: {g.d(2)}")
print(f"Peso da aresta (1, 2): {g.w(1, 2)}")
print(f"Menor grau: {g.mind()}")
print(f"Maior grau: {g.maxd()}")

distances_bfs, predecessors_bfs = g.bfs(1)
print("Distâncias BFS a partir de 1:", distances_bfs)
print("Predecessores BFS a partir de 1:", predecessors_bfs)

predecessors_dfs, start_time, end_time = g.dfs(1)
print("Predecessores DFS a partir de 1:", predecessors_dfs)
print("Tempos de início:", start_time)
print("Tempos de término:", end_time)

distances_bf, predecessors_bf = g.bf(1)
print("Distâncias Bellman-Ford a partir de 1:", distances_bf)
print("Predecessores Bellman-Ford a partir de 1:", predecessors_bf)

distances_dijkstra, predecessors_dijkstra = g.djikstra(1)
print("Distâncias Dijkstra a partir de 1:", distances_dijkstra)
print("Predecessores Dijkstra a partir de 1:", predecessors_dijkstra)

print(" ")


def read_digraph(caminho_arquivo):
    G = Digraph(weighted=True)
    with open(caminho_arquivo, 'r') as file:
        for _ in range(7):
            file.readline()
        for line in file:
            parts = line.split()
            if parts[0] == 'a':
                x, y, p = map(int, parts[1:])
                G.add_edge(x, y, p)
    return G


caminho_arquivo = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "USA-road-d.NY",
    "USA-road-d.NY.gr",
)

G = read_digraph(caminho_arquivo)

print("a) O valor de G.mind():", G.mind())
print("b) O valor de G.maxd():", G.maxd())


def encontrar_caminho_com_arestas_minimas(digrafo, min_arestas=10):
    for v in digrafo.adj:
        distances, predecessors = digrafo.bfs(v)
        for w in distances:
            caminho = []
            current = w
            while current is not None:
                caminho.append(current)
                current = predecessors[current]
            caminho.reverse()
            if len(caminho) >= min_arestas:
                return caminho
    return None


caminho = encontrar_caminho_com_arestas_minimas(G)
print("c) Caminho com 10 ou mais arestas:", caminho)


def cycle(pi, v_ini, v_fim):
    for u in v_ini:
        for v in G.adj[u]:
            if pi[u] != v and v_ini[v] < v_ini[u] and v_fim[v] > v_fim[u]:
                ciclo = []
                atual = u
                while atual is not None and atual != v:
                    ciclo.append(atual)
                    atual = pi[atual]
                ciclo.append(v)
                ciclo.reverse()
                if len(ciclo) >= 5:
                    return ciclo
    return None


def encontrar_ciclo_com_arestas_minimas(digrafo):
    for v in digrafo.adj:
        pi, v_ini, v_fim = digrafo.dfs(v)
        ciclo_encontrado = cycle(pi, v_ini, v_fim)
        if ciclo_encontrado:
            return ciclo_encontrado
    return None


ciclo_5_arestas = encontrar_ciclo_com_arestas_minimas(G)
print("d) Ciclo com 5 ou mais arestas:", ciclo_5_arestas)


def encontrar_vertice_mais_distante(digrafo, v):
    distances, _ = digrafo.djikstra(v)
    max_dist = max(distances.values())
    vertice_mais_distante = [k for k, d in distances.items() if d == max_dist]
    return vertice_mais_distante[0], max_dist


vertice, distancia = encontrar_vertice_mais_distante(G, 129)
print(f"e) O vértice mais distante de 129 é o {vertice}, e a distância é {distancia}")
