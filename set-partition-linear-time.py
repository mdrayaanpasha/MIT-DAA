import math

arr = [80,23,42,123,23]
Sum = sum(arr)
N = len(arr)
L = math.floor(N / 2) 
Target = Sum / 2  
Sel = []  


for i in range(N - 1, -1,-1):
    if Target - arr[i] >= 0:
        Sel.append(arr[i])
        Target -= arr[i]
        L -= 1

print(Sel)
