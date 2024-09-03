import queue

G = {
    'A':[['B','C'],{"visited":False,"Parent":None}],
    'B':[['D','C'],{"visited":False,"Parent":None}],
    'C':[[],{"visited":False,"Parent":None}],
    'D':[[],{"visited":False,"Parent":None}],
}


Q = queue.Queue()


def DFS(G,Q,src):
    G[src][1]["visited"]=True
    
    for neighbor in G[src][0]:
        Q.put({'From':src,'To':neighbor})
    
    while Q.qsize() != 0:
        rem=Q.get()
        # print()
        if not G[rem["To"]][1]["visited"]:
            G[rem["To"]][1]["Parent"]=rem["From"]
            DFS(G,Q,rem["To"])

        
DFS(G,Q,'A')


for keys in G:
    print(G[keys])


        
    
            
    
            
