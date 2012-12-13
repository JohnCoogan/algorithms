#!/usr/bin/python
# Graph algorithms

import Queue

class Vertex:
    def __init__(self,val):
        self.key = val
        self.color = "white"
        self.d = 0
        self.p = None
    def __str__(self):
        return str(self.key)

graph = {}

v0 = Vertex(0)
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)

# init graph using adjacency-list representation
graph[v0]=[v1]
graph[v1]=[v0,v2]
graph[v2]=[v1,v3]
graph[v3]=[v2,v4,v5]
graph[v4]=[v3,v5,v6]
graph[v5]=[v3,v4,v6,v7]
graph[v6]=[v4,v5,v7]
graph[v7]=[v5,v6]

# Breadth-first search
def bfs(G,s):
    for vertex,edges in graph.items():
        if vertex != s:
            vertex.color = "white"
            vertex.d = float("inf")
            vertex.p = None
    s.color = "gray"
    s.d = 0
    s.p = None
    q = Queue.Queue(0)
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if v.color == "white":
                v.color = "gray"
                v.d = u.d + 1
                v.p = u
                q.put(v)
        u.color = "black"

bfs(graph, v2)

for vertex,edges in graph.items():
    print vertex, vertex.d