SubSets={
    0:[2,3,4],
    1:[2,4],
    2:[3,1],
    3:[1,2],
    4:[]
}
U=[1,2,3,4]
selected=[]

while len(selected) != len(U):
    Max=0;
    MaxEle=None
    for keys in SubSets:
        if len(SubSets[keys]) > Max:
            Max=len(SubSets[keys])
            MaxEle=SubSets[keys]
            SubSets[keys]=[]
            for ele in MaxEle:
                if ele not in selected:
                    selected.append(ele)
           
            
print(selected)
