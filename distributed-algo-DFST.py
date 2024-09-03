G = {
    'A':[['B','C'],{"visited":False,"Parent":None}],
    'B':[['D','C'],{"visited":False,"Parent":None}],
    'C':[[],{"visited":False,"Parent":None}],
    'D':[[],{"visited":False,"Parent":None}],
}


for key in G:
    for neighbor in G[key][0]:
        if not G[neighbor][1]["visited"]:
            G[neighbor][1]["visited"]=True
            G[neighbor][1]["Parent"]=key
            print("Parent of: ",neighbor," Is: ",key)
            
    
            
