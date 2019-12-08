n,k=map(int,input().split())
a=list(range(1,n+1))
num=1
while len(a)>0:
    key_del=[]
    #key_del存储要删除元素的索引
    for key,value in enumerate(a):
        if(num%k==0 or num%10==k):
            key_del.append(key)
        num+=1

    for key in key_del:
        del a[key]
        if len(a)==1:
            print(a[0])