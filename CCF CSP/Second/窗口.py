N,M=map(int,input().split())
window,coordinate=[],[]
for i in range(N):
    s=list(map(int,input().split()))
    window.append(s)
for j in range(M):
    s=list(map(int,input().split()))
    coordinate.append(s)
for coor in coordinate:
    m=0
    for w in window:
        if w[0]<=coor[0]<=w[2] and w[1]<=coor[1]<=w[3]:
            m=window.index(w)+1
        if m==0:
            m='IGNORED'
    coor.append(m)
for co in coordinate:
    print(co[2])
'''
3 4
0 0 4 4
1 1 5 5
2 2 6 6
1 1
0 0
4 4
0 5
'''          

            

    