N,M =map(int,input().split())
T,K,P=0,0,0
for i in range(N):
    a=list(map(int,input().split()))
    a0,am=a[0],a[1:]
    
    T+=a0
    am=map(abs,am)
    p=sum(am) #此树掉落个数
    T-=p
    if P<p:
        P=p
        K=i+1
print("{} {} {}".format(T,K,P))
