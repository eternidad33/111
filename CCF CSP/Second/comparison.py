n = int(input())
m = int(input())
line = []
for i in range(n):
    line.append(i+1)
for i in range(m):
    stu,pos = map(int,input().split())
    after = line.index(stu) + pos
    line.remove(stu)
    line.insert(after,stu)
print(" ".join(map(str,line)))