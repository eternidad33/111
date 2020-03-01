list1=[[1,2,3],[4,5,6],[7,8,9]]
max,min=0,100
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j]>max:
            max=list1[i][j]
        if list1[i][j]<min:
            min=list1[i][j]
print(max)
print(min)