#Z字形扫描
n = int(input())
rect = []
for i in range(n):
    rect.append(list(map(int,input().split())))
i,j = 0,0
line = []#经历过的数字
up = True#方向向上
for t in range(n*n):
    line.append(rect[i][j])
    #碰壁后就转向
    if up:#右上
        if j==n-1:    # 碰到了右边界
            i += 1        # 向下走一格
            up=False      # 转向
        elif i==0:    # 碰到了上边界
            j += 1        # 向右走一格
            up=False      # 转向
        else:         # 没碰到边界
            j += 1        # 向右上斜着走一格
            i -= 1
    else:#左下
        if i==n-1:    # 碰到了下边界
            j += 1        # 向右走一格
            up=True       # 转向
        elif j==0:    # 碰到了左边界
            i += 1        # 向下走一格
            up=True       # 转向
        else:         # 没碰到边界
            j -= 1        # 向左下斜着走一格
            i += 1
print(" ".join(map(str,line)))

    