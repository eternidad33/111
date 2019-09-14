def h(s):
    if len(s)<2:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return h(s[1:-1])
if __name__=='__main__':
    s=input("请输入一个整数")
    if h(s):
        print("这个数是回文数")
    else:
        print("这个数不是回文数")
