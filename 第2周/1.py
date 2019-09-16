list1=[[1,2,3],[4,5,6],[7,8,9]]
sum1=0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i==j:
            sum1+=list1[i][j]
print(sum1)