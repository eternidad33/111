#判断是否含有数字
def pan(s):
    for i in range(len(s)):
        if 0<=s[i]<=9:
            return True
    return False

#提取数字
def Tiqu(s):
    list1=list()
    for i in range(len(s)):
        for j in range(i:len(s)):
            if 0<=s[i]<=9:
                st=i
            elif 0<=s[j]<=9 and s[j+1]>9 and s[j+1]<0:
                end=j    
            list1.append(s[st:end])
    return list1
   
if __name__ == "__main__":
    s=input("请输入一段字符串：")
    if pan(s):
        li=Tiqu(s)
    else :
        print("字符串中不含有数字")
    print(li)