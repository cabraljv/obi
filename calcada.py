n=int(input())
v=[]
for i in range(n):
    v.append(int(input()))


#Remove duplicate numbers
vSet = set(v)

if len(vSet)==1:
    print(1)
else:

    pairs=set()

    for i in vSet:
        for j in vSet:
            if(i != j and not (j,i) in pairs):
                pairs.add((i,j))

    #If the set has more than 1 number, the min best result is 1
    best=1

    for i in pairs:
        bestP=0
        for j in v:
            position = v.index(j)
            if j in i:
                if position>0:
                    if position<len(v)-1:
                        if not v[position+1] in i and not v[position-1] in i:
                            bestP+=1
                    else:
                        if not v[position-1] in i:
                                bestP+=1 
                else:
                    if not v[position+1] in i:
                            bestP+=1 
        best = max(bestP, best)

    print(best)
