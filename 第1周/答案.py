#E0101
#1.編写程序,将100至200之同能够被3整除,但不能被5整除的数据及其个数输出
n=0 #n用于记录符合要求数字的个数
strresult=''#将符合要求的数字转为字符审记灵在 strresult中,以“,”为分割符,最后输出
for i in range(100,201):#是否需要包含200由题与确定
    if i%3==0 and i %5 !=0:
        n=n+1
        strresult=strresult+str(i)+','
print('符合要求的数字共有{}个'.format(n))
print('如下所示:')
print( strresult[:-1])# strresult最后一个符号为返号,不输出

#2.编写程序,接收用户输入的两个整数值,如果第一个数值为奇数,输出结果为第一个数值减去第二个数值的差;
#如果第一个数值为偶数,输出结果为第一个数值加第二个数值的和
n1=int(input("请输入第一个整数:")
n2=int(input("请输入第二个整数:"))
if nl%2==1:    #第一个数为奇数
    print('{}-{}={}'.format(nl,n2, n1-n2))
else:    #第一个数为偶数
    print('{}-{}={}'.format(nl, n2, n1+n2))

#E0103
#3.編写程序,找出100以内的“完数”并输出,同时输出找出的完数个数。
#所谓“完数”就是数本身等于真各因子之和的数,如6=1+2+3。
nofperfectNum=0#初始完全数个数为0
strresult=''#将符合要求的数字转为字符记灵在 strresuit中,以“,"”为分割符,最后输出
for n in range(2,1001):#是否包含1000由题目确定,n依次取得1到1000的每一个数字,1不是完
    sumo=1#对每一个检査是否为完数的n,部需要因子之和初始化为1
    for i in range (2, n-1):
        if n%i=0:   #可以整除所,i为因子
            sumo += i
    if sumo == n:
        nofperfectNum +=1
        strresult= strresult+str(n)+','
print('共有完全数{}个。'.format(nofperfectNum))
print('分别是:')
print(strresult[:-1])

#E0104
#1.编写程序,输出斐 波那契(Fibonacci)数列的前n项,n的值鍵盘输入,数列的定义如下:
#a1=1,a2=1,an=an-1+an-2(n>=3)
n=int(Input('请输入一个整数(>=3):'))
a1,a2=1,1 #菱波那契数列前两项a1和2均为1
print('前{}项斐波那契额数列分别为:'. format(n))
print('{},{}'.format(al,a2), end='')
for i in range (3,n+1):
    an=a1+a2
    a1=a2
    a2=an
    print(',{}'.format(an), end='')

#E0105
#2.编写程序,判断一个从鍵盘输入的整数是否为回文数。
n=Input('请输入一个整数:')
if n.isdigit():  #如果字符密n中全是数字
    if n==n[::-1]:
        print('{}是回文数。'.format(n))
    else:5
        print('{}不是回文数。'.format(n))
else:
print('你输入的{},不是整数数字。'. format(n))
