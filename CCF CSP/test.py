n=int(input())
for i in reversed(range(n+1)):
    for j in range(i):
        print(i,end=' ')
    print()
    print(' '*(n+1-i),end='')
    