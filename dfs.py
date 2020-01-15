from graph import *

gr = Graph({1, 2, 3, 4, 5, 6, 7}, {(1, 2), (1, 4), (2, 3), (4, 3), (4, 5), (6, 7)})
print(gr.adj_l)

visited = set()

def dfs(starting_vertex, G):
    # component search with dfs
    visited.add(starting_vertex)
    for ver in G.adj_l[starting_vertex]:
        if ver not in visited:
            dfs(ver, G)
    return visited

print( dfs(1, gr) )
