#训练集
list1=[[1.2,3.1,"A"],[2.3,3.1,"A"],[1.8,2.6,"A"],[1.5,2.7,"A"],[1.3,3.1,"A"],[2.6,3.7,"A"],[2.5,1.5,"B"],[3.5,2.7,"B"],[2.9,1.8,"B"],[3.1,2.3,"B"]]
#测试集
list2=[[1.8,2.6,"A"],[3.6,2.1,"B"],[2.4,2.2,"B"]]
def oshi(x,y):
    minA=list()
    minB=list()
    min_1=1000;min_2=1000
    #计算与A类点坐标的距离
    for i in range(len(list1)-4):
        a=list1[i][0]
        b=list1[i][1]
        s=(x-a)**2+(y-b)**2
        minA.append(s)
        
    #计算与B类点坐标的距离
    for i in range(len(list1)-4,len(list1)):
        a=list1[i][0]
        b=list1[i][1]
        s=(x-a)**2+(y-b)**2
        minB.append(s)
    #与A点的距离进行升序排列，并取前三个
    minA.sort()
    minA=minA[:3]
    #与B点的距离进行升序排列，并取前三个
    minB.sort()
    minB=minB[:3]
    
    sumA=0;sumB=0
    for i in minA:
        sumA+=i
    for i in minB:
        sumB+=i
    if sumA<=sumB:
        return "A"
    else:
        return "B"

if __name__ == "__main__":
    count=0
    list3=list2
    for i in range(len(list2)):
        x=list2[i][0]
        y=list2[i][1]
        ss=oshi(x,y)
        if ss==list2[i][2]:
            count+=1
        list3[i][2]=ss
    op=format(count/3,'.2%')
    print(list3)
    print("准确率为",op)