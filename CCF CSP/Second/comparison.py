#窗口
n,m = list(map(int,input().split()))
w=[]
for i in range(n):
    w.append(list(map(int,input().split())))#点数据输入
    w[i].append(i+1)#窗口标识
for i in range(m):
    x,y = list(map(int,input().split()))#查询点
    find = False
    for i,s in reversed(list(enumerate(w))):#窗口叠放顺序反向查找
        if(x>=s[0] and x<=s[2] and y>=s[1] and y<=s[3]):#点在该窗口内
            print(s[4])
            last = w[i]
            for j in range(i,len(w)-1):
                w[j] = w[j+1]
            w[-1] = last#窗口移到最顶端
            find = True
            break
    if(not find):
        print("IGNORED")