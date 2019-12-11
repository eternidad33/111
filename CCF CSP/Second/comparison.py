#工资计算
t = int(input())
 
level = [0,1500,4500,9000,35000,55000,80000,1000000]
rate = [0,0.03,0.1,0.2,0.25,0.30,0.35,0.45]
aftertax = [3500]
sum=0
for i in range(1,len(level)):
	sum += int((level[i]-level[i-1])*(1-rate[i]))
	aftertax.append(sum + 3500)
 
if(t<=3500):
	s=t
else:
	for i in range(len(aftertax)):
		if(t>aftertax[i] and t<=aftertax[i+1]):
			s=3500+level[i]
			s+=int((t - aftertax[i])/(1 - rate[i+1]))
			s= 100*(round(s/100))
			break
print(s)