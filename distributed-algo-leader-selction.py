import random
import math

G ={
    'A':[['B','C','A'],[None,None,[]]],
    'B':[['B','C','A'],[None,None,[]]],
    'C':[['B','C','A'],[None,None,[]]],
}

#lets give its id some random values

for key in G:
    RID=random.randint(0,len(G)*5)
    G[key][1][0]=RID
    
#now lets send some messages

for key in G:
    Message={key:G[key][1][0]}
    for otherKeys in G:
        G[otherKeys][1][2].append(Message)


#now lets make them select their leaders:
for key in G:
    Messages = G[key][1][2]
    Max=-math.inf
    leadId=-1
    for i in range(len(Messages)):
        ele = list(Messages[i])[0]
        if Messages[i][ele] > Max:
            Max=Messages[i][ele]
            leadId=ele
            
    G[key][1][1]=leadId
    G[key][1][2]=[]
    
    
for key in G:
    print(key,G[key])

