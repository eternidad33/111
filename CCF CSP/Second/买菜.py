n=int(input())
H,W=[],[]
for i in range(n):
    H.append(list(map(int,input().split())))
for i in range(n):
    W.append(list(map(int,input().split())))
tsum=0
for h in H:
    for w in W:
        if h[0]>=w[0]:
            if w[1]>=h[0] and w[1]<=h[1]:
                tsum+=(w[1]-h[0])
            if w[1]>=h[1]:
                tsum+=(h[1]-h[0])
        else :
            if h[1]>=w[0] and h[1]<=w[1]:
                tsum+=(h[1]-w[0])
            if h[1]>=w[1]:
                tsum+=(w[1]-w[0])
print(tsum)
