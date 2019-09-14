def addd(a,b):
    if a%2==1:
        return a-b
    else:
        return a+b
if __name__ == "__main__":
    a=int(input("请输入第一个数："))
    b=int(input("请输入第二个数："))
    n=addd(a,b)
    print("结果为")
print(n)
