n=0
for i in range(100,201):
    if i%3==0 and i%5!=0:
        print(i)
        n=n+1
print('个数为')
print(n)
