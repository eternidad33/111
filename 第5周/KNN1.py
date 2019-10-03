
def oshi(x,y):
    sa=(x-1.2)**2+(y-3.1)**2
    sb=(x-2.5)**2+(y-1.5)**2
    if sa<=sb:
        return True
    else:
        return False

if __name__=="__main__":
    list1=list()
    while True:
        list2=list()
        x=float(input("请输入x点的横坐标"))
        y=float(input("请输入x点的纵坐标"))
        list2.append(x)
        list2.append(y)
        if oshi(x,y):
            print("x属于A类")
            list2.append('A')
        else:
            print("x属于B类")
            list2.append('B')
        list1.append(list2)