# import math
# def zs(t):
#     i=1
#     while i<=int(math.sqrt(t)):
#         i = i + 1
#         if (t % i) == 0:
#             print(i,end=" " )
#             t=t/i
#             i=1
#     if(t>1):
#         print(int(t))
#
# a=int(input())
# while a<1 or a>2000000014:
#     print("请从新输入")
#     a=int(input())
# zs(a)
# for i in range(1000):
#     print(i,end=": ")
#     zs(i)
#     print()

# a=input()
# while len(a)>5000:
#     a=input()
# b=a.split(' ')
# print(len(b[len(b)-1]))

import  random

# a=int(input())
# i=0
# b=list()
# while i<a:
#
#     c=int(input())
#     b.append(c)
#     i=i+1
#
# b=list(set(b))
# b.sort()
# for i in b:
#     print(i)

# a=input()
# N=int(a.split(' ')[0])
# m=int(a.split(' ')[1])
# b=list()
# for i in range(m):
#     print(i)
#     c=input()
#     d=c.split(' ')
#     d.append(i+1)
#     b.append(d)

# a=input()
# b=a.split(';');
# x=0
# y=0
# for i in b:
#     #print(i[1:3])
#     if len(i)!=3 and len(i)!=2:
#         continue
#     if i[0] =='A':
#
#         try:
#             x=x-int(i[1:3])
#         except:
#             continue
#     if i[0] =='D':
#
#         try:
#             x=x+int(i[1:3])
#         except:
#             continue
#     if i[0] =='W':
#
#         try:
#             y=y+int(i[1:3])
#         except:
#             continue
#     if i[0] =='S':
#
#         try:
#             y=y-int(i[1:3])
#         except:
#             continue
#
# print(str(x)+','+str(y))



import sys
x = sys.stdin

a = 0
b = 0
c = 0
d = 0
e = 0
m = 0
n = 0
for i in x:
    p = i.split('~')
    try:
        print(p[0].split('.')[0] + "\t" + p[1].split('.')[0])
        for j in p[0].split('.'):
            try:
                if int(j) < 0 or int(j) > 255:
                    m = m + 1
            except:
                m = m + 1
                continue


        if int(p[0].split('.')[0]) >= 1 and int(p[1].split('.')[0]) <= 126:
            a = a + 1
        elif int(p[0].split('.')[0]) >= 128 and int(p[1].split('.')[0]) <= 191:
            b = b + 1
        elif int(p[0].split('.')[0]) >= 192 and int(p[1].split('.')[0]) <= 223:
            c = c + 1
        elif int(p[0].split('.')[0]) >= 224 and int(p[1].split('.')[0]) <= 239:
            d = d + 1
        elif int(p[0].split('.')[0]) >= 240 and int(p[1].split('.')[0]) <= 255:
            e = e + 1
        else:
            m = m + 1

        if int(p[0].split('.')[0]) >= 10 and int(p[1].split('.')[0]) <= 255:
            n = n + 1
        elif int(p[0].split('.')[0]) == 172 and int(p[1].split('.')[0]) == 172:
            if int(p[0].split('.')[1]) >= 16 and int(p[1].split('.')[1]) <= 31:
                n = n + 1
        elif int(p[0].split('.')[0]) == 192 and int(p[1].split('.')[0]) == 192:
            if int(p[0].split('.')[1]) == 168 and int(p[1].split('.')[1]) == 168:
                n = n + 1
    except:
        pass
        continue
print(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e) + " " + str(m) + " " + str(n))
#



# import sys
# import re
# a,b,c,d,e,eip,ip=0,0,0,0,0,0,0
# def aa(aa):
#     global eip
#     for i in range(4):
#         if not aa[i].isdigit():
#             eip+=1
#             return False
#     return True
# def ss(uu):
#     for i in range(len(uu)-1):
#         if uu[i]=="0":
#             if uu[i+1]=="1":
#                 return False
#         if i==len(uu)-2:
#             if uu.startswith("0")or uu.endswith("1"):
#                 return False
#     return True
# for u in sys.stdin:
#     u=re.split("[.~]",u[0:-1])
#     ui=u[0:4]
#     uy=u[4:]
#     unn=uyy=list(map(lambda x:bin(int(x))[2:],uy))
#     for i in range(4):
#         if len(uyy[i])<8:
#             s="".join(["0" for i in range(8-len(uyy[i]))])
#             uyy[i]=s+uyy[i]
#     uu="".join(uyy)
#     if ss(uu):
#         if aa(ui):
#             if int(ui[0])>=1 and int(ui[0])<=126:
#                 a+=1
#                 if int(ui[0])==10:
#                     ip+=1
#             elif int(ui[0])>=128 and int(ui[0])<=191:
#                 b+=1
#                 if int(ui[0])==172 and int(ui[1])>=16 and int(ui[1])<=31:
#                     ip+=1
#             elif int(ui[0])>=192 and int(ui[0])<=223:
#                 c+=1
#                 if int(ui[0])==192 and int(ui[1])==168:
#                     ip+=1
#             elif int(ui[0])>=224 and int(ui[0])<=239:
#                 d+=1
#             elif int(ui[0])>=240 and int(ui[0])<=255:
#                 e+=1
#             elif int(ui[0])==0:
#                 continue
#             else:
#                 eip+=1
#     else:
#         eip+=1
# print(a,b,c,d,e,eip,ip)
#



