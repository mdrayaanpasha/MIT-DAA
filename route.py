import random

def generate_risk():
   
    weather = random.uniform(0, 10)
    piracy = random.uniform(0, 10)
    congestion = random.uniform(0, 10)
    
 
    risk = (weather * 0.5) + (piracy * 0.3) + (congestion * 0.2)
    return risk

G = {
    'MUM': [
        {
            'CHE': (generate_risk(), 1190),
            'KOL': (generate_risk(), 1320),
            'MUM': (0, 0)
        },
        {'shortestPath': 0, 'parent': 'MUM'}
    ],
    'CHE': [
        {
            'MUM': (generate_risk(), 1190),
            'VIS': (generate_risk(), 550),
            'CHE': (float('inf'), float('inf'))
        },
        {'shortestPath': float('inf'), 'parent': 'CHE'}
    ],
    'KOL': [
        {
            'COC': (generate_risk(), 1280),
            'VIS': (generate_risk(), 530),
            'KOL': (float('inf'), float('inf'))
        },
        {'shortestPath': float('inf'), 'parent': 'KOL'}
    ],
    'COC': [
        {
            'MUM': (generate_risk(), 360),
            'CHE': (generate_risk(), 440),
            'COC': (float('inf'), float('inf'))
        },
        {'shortestPath': float('inf'), 'parent': 'COC'}
    ],
    'VIS': [
        {
            'MUM': (generate_risk(), 1150),
            'CHE': (generate_risk(), 550),
            'KOL': (generate_risk(), 530),
            'COC': (generate_risk(), 720),
            'VIS': (float('inf'), float('inf'))
        },
        {'shortestPath': float('inf'), 'parent': 'VIS'}
    ]
}

def Optimizar(G):
    for keys in G:
        for neighbor in G[keys][0]:
            risk, distance = G[keys][0][neighbor]
            K2Ncost = risk * distance
            
            KeyCost = G[keys][1]['shortestPath'] * G[G[keys][1]['parent']][0][keys][0]
            neighborCost = G[neighbor][1]['shortestPath'] * G[G[neighbor][1]['parent']][0][neighbor][0]

            if neighborCost > KeyCost + K2Ncost:
                G[neighbor][1]['shortestPath'] = G[keys][1]['shortestPath'] + distance
                G[neighbor][1]['parent'] = keys

Optimizar(G)


print("Designed By Rayaan Pasha.\n")
print("This code is designed to compute the shortest route with optimal risk management for 5 major Indian ports:\nMumbai, Kolkata, Chennai, Cochin, Vishakapatnam\n")

print(f"{'Port':<10} {'From':<15} {'Cost (Kms)'}")
print("-" * 35)

for node in G:
    parent = G[node][1]['parent']
    shortest_path = G[node][1]['shortestPath']
    print(f"{node:<10} {parent:<15} {shortest_path:<10}")
