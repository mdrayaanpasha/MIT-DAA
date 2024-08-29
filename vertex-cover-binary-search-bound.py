G = {
    1:[2,3,4],
    2:[3],
    3:[4],
    4:[3]
}

def Arbitraty(G):
    for key in G:
        if len(G[key]) > 0:
            return key

def recurse(G,Arb,K):
    if K!=0:
        if Arb != None:
            G.pop(Arb)
            K-=1
            recurse(G,None,K)
        else:
            Arb = Arbitraty(G)
            G.pop(Arb)
            K-=1
            recurse(G,None,K)
    else:
        return len(G)
            

    
def Makeit(G):
    K=3
    ArbU=Arbitraty(G)
    ArbV = G[ArbU][0]
    D=G
    v1Cover = recurse(D,ArbU,K)
    D=G
    v2Cover = recurse(D,ArbV,K)
    
    if V1Cover > 0:
        print("vertex 1: ",ArbU," Is a vertex cover")
    else:
        print("vertex 1: ",ArbU," Is not a vertex cover")

    
Makeit(G)
        
