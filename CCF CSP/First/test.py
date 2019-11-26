N,M=map(int,input().split())
T,k,P=0,0,0
for i in range(N):
    a=list(map(int,input().split()))
    a0,am=a[0],a[1:]
    T+=a0
    am=map(abs,am)
    temp=sum(am)
    T-=temp
    if temp>=P:
        P=temp
        k=i+1
print(T,k,P)
    