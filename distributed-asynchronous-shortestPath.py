import queue
import math

G = {
    'A':[{'B':2,'C':1},{"dist":math.inf,"Parent":None}],
    'B':[{'D':1,'C':3},{"dist":math.inf,"Parent":None}],
    'C':[[],{"dist":math.inf,"Parent":None}],
    'D':[[],{"dist":math.inf,"Parent":None}],
}

Messages = queue.Queue()

def AsyncDijkstra(G,M,u):
    
    for neighbors in G[u][0]:
        M.put({'Parent':u,'To':neighbors, 'dist':G[u][0][neighbors]})
        
    while M.qsize() != 0:
        PopItem=M.get()

        currDistance = G[PopItem['To']][1]['dist']
        PotentialDistance = G[PopItem['Parent']][1]['dist'] + PopItem["dist"]
        
        if currDistance > PotentialDistance:
            G[PopItem['To']][1]['dist'] = PotentialDistance
            G[PopItem['To']][1]['Parent']=PopItem['Parent']
        AsyncDijkstra(G,M,PopItem['To'])
        
    
    
G['A'][1]["dist"]=0       
AsyncDijkstra(G,Messages,'A')

# for i in range(Messages.qsize()):
#     print(Messages.get())

for keys in G:
    print(G[keys])
