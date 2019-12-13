import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,100000)
w=[]
for i in x:
    if i<=0:
        w.append(0)
    elif 0<i<=1500:
        w.append(i*0.03)
    elif 1500<i<=4500:
        w.append(45+(i-1500)*0.1)
    elif 4500<i<=9000:
        w.append(345+(i-4500)*0.2)
    elif 9000<i<=35000:
        w.append(1245+(i-9000)*0.25)
    elif 35000<i<=55000:
        w.append(7745+(i-35000)*0.3)
    elif 55000<i<=80000:
        w.append(13745+(i-55000)*0.35)
    else:
        w.append(22495+(i-80000)*0.45)
plt.figure(figsize=(6,6))
plt.plot(x,w)
plt.show()
