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
t=[0]*N
for i in lin:
    t[i]=1
if t[-1]==t[0]==t[1]==1:
    E+=1
if t[-2]==t[-1]==t[0]==1:
    E+=1
for i in range(1,N-1):
    if t[i-1]==t[i]==t[i+1]==1:
        E+=1
print("{} {} {}".format(T,D,E))