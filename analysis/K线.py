file = 'C:\\Users\\wind\\Desktop\\py\\周K线.csv'
out1='C:\\Users\\wind\\Desktop\\py\\周K线\\1.txt'
out2='C:\\Users\\wind\\Desktop\\py\\周K线\\2.txt'
out3='C:\\Users\\wind\\Desktop\\py\\周K线\\3.txt'
#[-10%,0)
out4='C:\\Users\\wind\\Desktop\\py\\周K线\\4.txt'
#[0,10%]
out5='C:\\Users\\wind\\Desktop\\py\\周K线\\5.txt'
data={}
f=open(file,'r',encoding='utf-8')
for i in f.readlines():
    print(i)