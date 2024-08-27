import random

def giveme(src, G, visited, path):
    visited[src] = True
    path.append(src)
    G[src] = []
    
    selected = None
    while selected is None and G[src]:
        select = random.choice(G[src])
        if not visited[select]:
            selected = select
    
    if selected is not None:
        giveme(selected, G, visited, path)
    
    for i in range(len(G)):
        if not visited[i]:
            giveme(i, G, visited, path)
            
G = {
    0: [1, 2, 3, 4],
    1: [2, 3],
    2: [3, 1],
    3: [],
    4: [5, 6]
}

visited = [False] * len(G)
start = random.choice(range(len(G)))
path = []

giveme(start, G, visited, path)

print("Vertex Cover Path:", path)
