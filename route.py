G = {
    'MUM': [
        {
            'CHE': (5, 1190),
            'KOL': (6, 1320),
            
            'MUM':(0,0)
        },
        {'shortestPath': 0, 'parent': 'MUM'}
    ],
    'CHE': [
        {
            'MUM': (5, 1190),
         
            'VIS': (6, 550),
            'CHE':(float('inf'),float('inf'))
        },
        {'shortestPath': float('inf'), 'parent': 'CHE'}
    ],
    'KOL': [
        {
            
            'COC': (6, 1280),
            'VIS': (7, 530),
            'KOL':(float('inf'),float('inf'))

        },
        {'shortestPath': float('inf'), 'parent': 'KOL'}
    ],
    'COC': [
        {
            'MUM': (3, 360),
            'CHE': (5, 440),
            'COC':(float('inf'),float('inf'))

        },
        {'shortestPath': float('inf'), 'parent': 'COC'}
    ],
    'VIS': [
        {
            'MUM': (6, 1150),
            'CHE': (6, 550),
            'KOL': (7, 530),
            'COC': (6, 720),
            'VIS':(float('inf'),float('inf'))

        },
        {'shortestPath': float('inf'), 'parent': 'VIS'}
    ]
}


def Optimizar(G):
    for keys in G:
        for neighbor in G[keys][0]:
            K2Ncost=G[keys][0][neighbor][1]*G[keys][0][neighbor][0]
            
            KeyCost=G[keys][1]['shortestPath'] * G[G[keys][1]['parent']][0][keys][0]
            
          
            neighborCost = G[neighbor][1]['shortestPath'] * G[G[neighbor][1]['parent']][0][neighbor][0]
            
          
            if neighborCost > KeyCost + K2Ncost:
                G[neighbor][1]['shortestPath']=G[keys][1]['shortestPath'] + G[keys][0][neighbor][1]
                G[neighbor][1]['parent']=keys
        
            
                
            
            
        
        
Optimizar(G)

print("Designed By Rayaan Pasha.\n")
print("This code is designed to compute the shortest route with optimal risk management for 5 major Indian ports:\nMumbai, Kolkata, Chennai, Cochin, Vishakapatnam\n")

print(f"{'Port':<10} {'From':<15} {'Cost (Kms)'}")
print("-" * 35)

for node in G:
    parent = G[node][1]['parent']
    shortest_path = G[node][1]['shortestPath']
    print(f"{node:<10} {parent:<15} {shortest_path:<10}")

