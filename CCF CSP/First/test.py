a,b,c,d=map(int,input().split())
if d<b:
    f=d+60-b
    e=c-a-1
else:
    f=d-b
    e=c-a
print(e," ",f)