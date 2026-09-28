import heapq
import sys

sys.setrecursionlimit(100000)

class Digraph:
    def __init__(self, weighted=True):
        self.adj = {}
        self.in_adj = {}
        self.degrees = {}
        self.weights = {}
        self.weighted = weighted

    def add_node(self, v):
        if v not in self.adj:
            self.adj[v] = []
            self.in_adj[v] = []
            self.degrees[v] = 0

    def add_edge(self, u, v, weight=1):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append(v)
        self.in_adj[v].append(u)
        self.degrees[u] += 1
        self.degrees[v] += 1
        if self.weighted:
            self.weights[(u, v)] = weight

    def n(self):
        return len(self.adj)

    def m(self):
        return sum(len(neighbors) for neighbors in self.adj.values())

    def viz(self, v):
        return set(self.in_adj[v]) | set(self.adj[v])

    def d(self, v):
        return self.get_indegree(v) + self.get_outdegree(v)

    def get_indegree(self, v):
        return len(self.in_adj[v])

    def get_outdegree(self, v):
        return len(self.adj[v])

    def w(self, u, v):
        return self.weights.get((u, v), None)

    def mind(self):
        return min(self.degrees.values())

    def maxd(self):
        return max(self.degrees.values())

    def bfs(self, v):
        distances = {node: float("inf") for node in self.adj}
        predecessors = {node: None for node in self.adj}
        distances[v] = 0
        queue = [v]
        while queue:
            u = queue.pop(0)
            for neighbor in self.adj[u]:
                if distances[neighbor] == float("inf"):
                    distances[neighbor] = distances[u] + 1
                    predecessors[neighbor] = u
                    queue.append(neighbor)
        return distances, predecessors

    def dfs(self, v):
        visited = set()
        pi = {node: None for node in self.adj} 
        v_ini = {}
        v_fim = {} 
        time = [0] 
        
        def dfs_visit(u):
            nonlocal time
            visited.add(u)
            v_ini[u] = time[0]
            time[0] += 1
            
            for neighbor in self.adj[u]:
                if neighbor not in visited:
                    pi[neighbor] = u
                    dfs_visit(neighbor)
            
            v_fim[u] = time[0]
            time[0] += 1
        
        dfs_visit(v)
        return pi, v_ini, v_fim

    def bf(self, v):
        distances = {node: float("inf") for node in self.adj}
        predecessors = {node: None for node in self.adj}
        distances[v] = 0

        for _ in range(len(self.adj) - 1):
            for u in self.adj:
                for neighbor in self.adj[u]:
                    if distances[u] + self.weights.get((u, neighbor), 1) < distances[neighbor]:
                        distances[neighbor] = distances[u] + self.weights.get((u, neighbor), 1)
                        predecessors[neighbor] = u

        return distances, predecessors

    def djikstra(self, v):
        distances = {node: float("inf") for node in self.adj}
        predecessors = {node: None for node in self.adj}
        distances[v] = 0
        pq = [(0, v)]
        while pq:
            current_dist, u = heapq.heappop(pq)
            if current_dist > distances[u]:
                continue
            for neighbor in self.adj[u]:
                new_dist = distances[u] + self.weights.get((u, neighbor), 1)
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = u
                    heapq.heappush(pq, (new_dist, neighbor))
        return distances, predecessors