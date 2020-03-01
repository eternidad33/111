if __name__ == "__main__":
    n=0
    for i in range(2,1001):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum==i:
            print(sum)
            n+=1
    print("完数个数为：")
    print(n)
