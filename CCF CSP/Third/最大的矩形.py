n=int(input())
H=list(map(int,input().split()))
maxArea,w=H[0],1
for i in range(1,n):
    if H[i]<=H[i-1]:
        w+=1
        temp=H[i]*w
        if temp>maxArea:
            maxArea=temp
    else:
        w=1
        if H[i]>maxArea:
            maxArea=H[i]
print(maxArea)