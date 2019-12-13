n,k=map(int,input().split())
ks=list(range(1,n+1))
enc=[]
for i in range(k):
    enc.append(list(map(int,input().split())))
for e in enc:
    for i in range(e[1],e[2]+1):
        ks[ks.index(e[0])]=0
    


