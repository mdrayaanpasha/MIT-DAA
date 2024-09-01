import math


G = {
    'A': [[('B', 2), ('C', 5)], {'SH': math.inf, 'Pr': None, 'Count': 0, 'P': None}],
    'B': [[('E', 10), ('D', 3)], {'SH': math.inf, 'Pr': None, 'Count': 0, 'P': None}],
    'C': [[('E', 6)], {'SH': math.inf, 'Pr': None, 'Count': 0, 'P': None}],
    'D': [[], {'SH': math.inf, 'Pr': None, 'Count': 0, 'P': None}],
    'E': [[('D', 7)], {'SH': math.inf, 'Pr': None, 'Count': 0, 'P': None}],
}

def Dijkstra(G,src):
    G[src][1]['SH']=0;
    for keys in G:
        for ele in G[keys][0]:
            if G[keys][1]["SH"] + ele[1] < G[ele[0]][1]["SH"]:
                G[ele[0]][1]["SH"]= G[keys][1]["SH"] + ele[1]
                G[ele[0]][1]["Pr"]=keys
            
def DFS(G, src):
    if G[src][1]['Count'] == len(G[src][0]):
        return True
    

    for neighbor, weight in G[src][0]:
        if G[neighbor][1]['P'] is None: 
            G[neighbor][1]['P'] = src 
            if DFS(G, neighbor):  
                G[src][1]['Count'] += 1
    return G[src][1]['Count'] == len(G[src][0])

DFS(G, 'A')
Dijkstra(G,'A')

for key in G:
    print(f"Node: {key}, Parent: {G[key][1]['P']}")
