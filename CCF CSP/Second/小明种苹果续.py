N=int(input())  #N为苹果树棵树
#T为总苹果数，D为发生掉落的苹果棵树，E为组数
T,D,E=0,0,0
lin=[]      
for i in range(N):
    a=list(map(int,input().split()))
    a0,am=a[0],a[1:]   #a0为操作次数
    b=False #判断D是否自增
    temp=am[0]
    for j in am:
        if j>0:
            if temp!=j:
               b=True
               temp=j
        else:
            temp+=j
    if b:
        lin.append(i)
        D+=1
    T+=temp
for i in range(1,len(lin)-1):
    if lin[i-1]+lin[i+1]==2*lin[i] |lin[-2]+lin[0]==2*lin[-1]|lin[-1]+lin[1]==2*lin[0]:
        E+=1
print("{} {} {}".format(T,D,E))

    