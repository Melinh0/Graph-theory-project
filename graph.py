import heapq
import sys

sys.setrecursionlimit(100000)

class Graph:
    def __init__(self, weighted=True):
        self.adj = {}
        self.degrees = {}
        self.weights = {}
        self.weighted = weighted  

    def add_node(self, v):
        if v not in self.adj:
            self.adj[v] = []
            self.degrees[v] = 0

    def add_edge(self, u, v, weight=1):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append(v)
        self.adj[v].append(u) 
        self.degrees[u] += 1
        self.degrees[v] += 1
        if self.weighted:
            self.weights[(u, v)] = weight
            self.weights[(v, u)] = weight  

    def n(self):
        return len(self.adj)

    def m(self):
        return sum(len(neighbors) for neighbors in self.adj.values()) // 2  

    def viz(self, v):
        return set(self.adj.get(v, []))

    def d(self, v):
        return self.degrees.get(v, 0)

    def w(self, u, v):
        return self.weights.get((u, v), 1)

    def mind(self):
        return min(self.degrees.values()) if self.degrees else 0

    def maxd(self):
        return max(self.degrees.values()) if self.degrees else 0

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
        predecessors = {node: None for node in self.adj}
        start_time = {}
        end_time = {}
        time = [0]

        def dfs_visit(u):
            time[0] += 1
            start_time[u] = time[0]
            for neighbor in self.adj[u]:
                if neighbor not in start_time:
                    predecessors[neighbor] = u
                    dfs_visit(neighbor)
            time[0] += 1
            end_time[u] = time[0]

        dfs_visit(v)
        return predecessors, start_time, end_time

    def bf(self, v):
        distances = {node: float("inf") for node in self.adj}
        predecessors = {node: None for node in self.adj}
        distances[v] = 0

        for _ in range(len(self.adj) - 1):
            for u in self.adj:
                for neighbor in self.adj[u]:
                    if distances[u] + self.weights[(u, neighbor)] < distances[neighbor]:
                        distances[neighbor] = distances[u] + self.weights[(u, neighbor)]
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