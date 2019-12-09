y=int(input())
d=int(input())
mon,day,daysum=0,0,0
md=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if y%4==0 and y%100!=0:
    md[2]=29
for i in range(13):
    if daysum<d:
        daysum+=md[i]
    else:
        mon=i-1
        day=md[i-1]-(daysum-d)
        break
print(mon)
print(day)
