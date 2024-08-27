import math

S = [2,4,6,3]

opt = math.floor(sum(S)/2);

N = len(S)

DP = [ [0] * N for _ in range(N) ]

Max = 0
MinSer= None
for i in range(N):
    for j in range(N):
        if i == j:
            DP[i][j]=S[i]
        elif j < i:
            DP[i][j]=0
        else:
            DP[i][j]=DP[i][j-1] + S[j]
        
        if DP[i][j] >= Max and DP[i][j] < opt:
            Max=DP[i][j]
            MinSer = (i,j)
            
        
set1 = []
set2 = []

for i in range(MinSer[0],MinSer[1]+1):
    set1.append(S[i])
    
for i in range(N):
    if i < MinSer[0] or i > MinSer[1]:
        set2.append(S[i])

print("Set 1 : ",set1,"Set 2: ",set2)
        




