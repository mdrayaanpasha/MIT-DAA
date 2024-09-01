G = {
    'A': [['D', 'C', 'B'], {'Count': 0, 'P': None}],
    'B': [[], {'Count': 0, 'P': None}],
    'C': [['B', 'F'], {'Count': 0, 'P': None}],
    'D': [['C'], {'Count': 0, 'P': None}],
    'E': [[], {'Count': 0, 'P': None}],
    'F': [['E'], {'Count': 0, 'P': None}]
}

def DFS(G, src):
    if G[src][1]['Count'] == len(G[src][0]):
        return True
    
  
    for neighbor in G[src][0]:
        if G[neighbor][1]['P'] is None:  
            G[neighbor][1]['P'] = src 
            if DFS(G, neighbor):  
                G[src][1]['Count'] += 1  
    return G[src][1]['Count'] == len(G[src][0])

DFS(G, 'A')

for key in G:
    print(f"Node: {key}, Parent: {G[key][1]['P']}")
