def fac(n):
    if n<=2:
        return 1
    else :
        return fac(n-1)+fac(n-2)
if __name__ == "__main__":
    n=int(input("请输入一个数:"))
    temp=fac(n)
    print(format(n),"的斐波那契数列为")
print(temp)   
