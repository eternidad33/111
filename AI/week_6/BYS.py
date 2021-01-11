list1 = [['A', 'H', '0', 'F'],
         ['A', 'H', '0', 'E'],
         ['B', 'H', '0', 'E'],
         ['C', 'M', '0', 'F'],
         ['C', 'L', '1', 'F'],
         ['C', 'L', '1', 'E'],
         ['B', 'L', '1', 'E'],
         ['A', 'M', '0', 'F'],
         ['A', 'L', '1', 'F'],
         ['C', 'M', '1', 'F'],
         ['A', 'M', '0', 'E'],
         ['B', 'M', '0', 'E'],
         ['B', 'H', '1', 'F'],
         ['C', 'M', '0', 'E']]
list2 = [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0]
X = ['A', 'M', '1', 'F']


# 计算数据
def calcu(x):
    l = len(list2)
    count = 0;
    l0 = list();
    l1 = list()
    for i in range(l):
        if list2[i] == 0:
            l0.append(list1[i])
            count += 1
        else:
            l1.append(list1[i])
    p0 = count / l  # 计算P(buy_computer=No)
    p1 = 1 - p0  # 计算P(buy_computer=Yes)
    bcount = l - count
    lx = len(x)
    sno = list();
    syes = list()
    no_temp = 1;
    yes_temp = 1;
    su = 0
    # 计算P(X|buy_computer=no)
    for i in range(lx):
        for j in l0:
            if x[i] == j[i]:
                su += 1
        no_temp *= su
        su = 0
    pxno = no_temp / (count ** lx)
    # 计算P(X|buy_computer=yes)
    for i in range(lx):
        for j in l1:
            if x[i] == j[i]:
                su += 1
        yes_temp *= su
        su = 0
    pxyes = yes_temp / (bcount ** lx)
    pno = pxno * p0
    pyes = pxyes * p1
    return pno, pyes


if __name__ == "__main__":
    no, yes = calcu(X)
    if yes > no:
        print("通过朴素贝叶斯分类预测buy_computer=yes")
    else:
        print("通过朴素贝叶斯分类预测buy_computer=no")
