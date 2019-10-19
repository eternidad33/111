import random

# 1、随机选取k个中心
# 2、计算每个点与之心点距离，将点分配到与其距离最近的中心所在的簇
# 3、计算每个簇的所有点的平均值，作为下一次中心，更新每个簇的中心
# 4、重复2、3，直到簇的分配不变

def oushi(D,i,j):
        li=[];lj=[]
        for k in D:
                s0=(i[0]-k[0])*(i[0]-k[0])+(i[1]-k[1])*(i[1]-k[1])
                s1=(j[0]-k[0])*(j[0]-k[0])+(j[1]-k[1])*(j[1]-k[1])
                if s0<=s1:
                        li.append(k)
                else:
                        lj.append(k)
        return li,lj

def Kmeans(D):        
        #任意取两个点
        i=random.choice(D)
        j=random.choice(D)
        while True:
                li=[];lj=[]
                #计算欧式距离
                li,lj=oushi(D,i,j)
                #取中心点
                sumx=0;sumy=0
                for i in li:
                        sumx+=i[0];sumy+=i[0]
                ui=[sumx/len(li),sumy/len(li)]
                sumx=0;sumy=0
                for j in lj:
                        sumx+=j[0];sumy+=j[0]
                uj=[sumx/len(lj),sumy/len(lj)]
                if(ui==i,uj==j):
                        break
                i=ui;j=uj
        return li,lj

if __name__ == "__main__":    
        list1=[[1.2,3.1],[2.3,3.1],[1.8,2.6],
        [1.5,2.7],[1.3,3.1],[2.6,3.7],
        [1.8,2.6],[2.5,1.5],[3.5,2.7],
        [2.9,1.8],[3.1,2.3],[3.6,2.1],[2.4,2.2]]
        l1,l2=Kmeans(list1)
        print("第一类数据有",l1)
        print("第二类数据有",l2)