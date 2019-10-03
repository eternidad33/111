import math
def oshi(x,y):
    sa=math.sqrt((x-1.8)**2+(y-2.6)**2)
    sb1=math.sqrt((x-3.6)**2+(y-2.1)**2)
    sb2=math.sqrt((x-2.4)**2+(y-2.2)**2)
    if sb1<=sb2:
        sbm=sb1
    else:
        sbm=sb2

    if sa<=sbm:
        return True
    else:
        return False
if __name__=="__main__":
    list1=[[1.2,3.1],[2.3,3.1],[1.8,2.6],[1.5,2.7],[1.3,3.1],[2.6,3.7],[2.5,1.5],[3.5,2.7],[2.9,1.8],[3.1,2.3]]
    for i in range(len(list1)):
        x=list1[i][0]
        y=list1[i][1]
        if oshi(x,y):
            list1[i].append('A')
        else:
            list1[i].append('B')
    print(list1)