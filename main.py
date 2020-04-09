# Author: S.Alireza Moazeni
from collections import defaultdict


# This class represents a undirected graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def add_edge(self, v, w):
        self.graph[v].append(w)  # Add w to v_s list
        self.graph[w].append(v)  # Add v to w_s list

    def get_cycle_members(self, start, end, parents_list):
        p = []
        p.append(start)
        moving_point = start
        while parents_list[moving_point] != end:
            p.append(parents_list[moving_point])
            moving_point = parents_list[moving_point]
        p.append(end)
        return p

    # A recursive function that uses visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def detect_cycle(self, v, visited, parents, parent):
        # Mark the current node as visited
        visited[v] = True
        parents[v] = parent
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not visited then recurse on it
            if not visited[i]:
                r1, cy = self.detect_cycle(i, visited, parents, v)
                if r1:
                    return True, cy
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                return True, self.get_cycle_members(v, i, parents)

        return False, []

    def is_cyclic(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        parents = [-1] * self.V
        # Call the recursive helper function to detect cycle in different
        # DFS trees
        for i in range(self.V):
            if not visited[i]:  # Don't recur for u if it is already visited
                r, cy = self.detect_cycle(i, visited, parents, -1)
                if r:
                    return r, cy

        return False, []


# Create a graph given in the above diagram
g = Graph(13)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(2, 7)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 11)
g.add_edge(4, 12)
g.add_edge(4, 6)
g.add_edge(5, 6)
g.add_edge(5, 10)
g.add_edge(7, 8)
g.add_edge(7, 9)
g.add_edge(8, 9)
g.add_edge(9, 10)

res = True

while res:
    res, member = g.is_cyclic()
    if res:
        print("cycle members {}".format(member))
        g.graph[member[0]].remove(member[-1])
        g.graph[member[-1]].remove(member[0])
