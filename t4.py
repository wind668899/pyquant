# def a(b):
#     x=''
#     k=1
#     for i in range(len(b)-1):
#         if b[i+1]==b[i]:
#             k=k+1
#         else:
#             x=x+str(k)+b[i]
#             k=1
#     x = x + str(k) + b[len(b)-1]
#     return x
# while True:
#     try:
#         n=int(input())+1
#         x='1'
#         for i in range(n):
#             if i==0:
#                 x='1'
#             else:
#                 x=a(x)
#         print(x)
#     except:
#         break

# while True:
#     try:
#         a=int(input())
#         for i in range(a):
#                 x=int((i+1)*i/2)
#                 y=int((i+2)*(i+1)/2)
#                 for k in range(a-i-1):
#                     print('    ', end='')
#                 for j in range(y-x):
#                     if j>0:
#                         print('    ',end='')
#                     if i%2==0:
#                         if x+1+j<10:
#                             print(str(x+1+j)+'***',end='')
#                         elif x+1+j<100:
#                             print(str(x+1+j)+'**',end='')
#                         elif x + 1 + j < 1000:
#                             print(str(x+1+j) + '*',end='')
#                         else:
#                             print(str(x+1+j),end='')
#                     else:
#                         if y  - j < 10:
#                             print(str(y  - j ) + '***', end='')
#                         elif y-j < 100:
#                             print(str(y  - j ) + '**', end='')
#                         elif y- j < 1000:
#                             print(str(y  - j ) + '*', end='')
#                         else:
#                             print(str(y  - j ), end='')
#                 print()
#     except:
#         break


# while True:
#     try:
#         k=input().split(':')
#         a=[int(k[0][0]),int(k[0][1]),int(k[1][0]),int(k[1][1])]
#         max=10000
#         r=k[0]+':'+k[1]
#
#         for i in range(4):
#             if a[i] > 2:
#                 continue
#             for j in range(4):
#                 if a[i] == 2 and a[j] > 4:
#                     continue
#                 for m in range(4):
#                     if a[m] > 6:
#                         continue
#                     for n in range(4):
#                         if a[i]>=a[0]:
#                             if a[j]>=a[1]:
#                                 if a[m]>=a[2] and a[n]>=a[3]:
#                                     k=60*(a[i]-a[0])*10+(a[j]-a[1])+10*(a[m]-a[2])+a[n]-a[3]
#                                 else:
#                                     k = 60*(a[i]-a[0])*10+(a[j]-a[1])+10*(a[m]-a[2])+a[n]-a[3]+24*60
#                             else:
#                                 k=60*(a[i]-a[0])*10+(a[j]-a[1])+10*(a[m]-a[2])+a[n]-a[3]+24*60
#                         else:
#                             k=60*(a[i]-a[0])*10+(a[j]-a[1])+10*(a[m]-a[2])+a[n]-a[3]+24*60
#                         if  max>k and k>0:
#                             max=k
#                             r=str(a[i])+str(a[j])+':'+str(a[m])+str(a[n])
#         print(r)
#     except:
#         break
#






#题目1  刘银辉 15817424993
# while True:
#     try:
#         a=input().split(' ')
#         k=int(input())
#         l=[]
#         for i in a:
#             l.append(int(i))
#         m=[]
#         for i in range(len(l)):
#
#             if i+k<=len(l):
#                 max=0
#                 for j in range(i,i+k):
#
#                     if j==i:
#                         max=l[j]
#                         continue
#                     if max<l[j]:
#                         max=l[j]
#                 m.append(max)
#         print(m)
#     except:
#         break

#题目2 刘银辉 15817424993
# def t(n):
#     if n == 2:
#         return 2
#     if n == 1:
#         return 1
#     else:
#         return t(n - 1) + t(n - 2)
#
#
# while True:
#     try:
#         n = int(input())
#
#         print(t(n))
#     except:
#         break






# while True:
#     try:
#         a=input()
#         t=0
#         for i in range(len(a)):
#             if i<len(a)-1:
#                 if a[i]=='(' and a[i+1]==')':
#                     t=t+1
#         print(t*2)
#     except:
#         break






# while True:
#     a=input().split('],[')
#     b=[]
#     for i in a:
#         b.append(list(map(int,i.replace('[','').replace(']','').split(','))))
#         print(i.replace('[','').replace(']',''))
#     #print(b)
#     l=[]
#
#     if len(b)==1:
#         print(b[0][0])
#     else:
#         for i in range (len(b)):
#             j=len(b)-2-i
#             #print()
#             print(l)
#             if j==len(b)-2:
#                 for k in range(len(b[j])):
#                     if k==0 :
#                         l.append(min(b[j+1][k],b[j+1][k+1])+b[j][k])
#                     else:
#                         l.append(min(b[j + 1][k-1], b[j + 1][k], b[j + 1][k + 1]) + b[j][k])
#
#             elif j>=0:
#                 #print(111)
#                 l2=[]
#                 for k in range(len(b[j])):
#                     if k == 0:
#                         #l[k] = min(l[k], l[k + 1]) + b[j][k]
#                         l2.append(min(l[k], l[k + 1]) + b[j][k])
#                     else :
#                         #l[k] = min(l[k - 1], l[k], l[k + 1]) + b[j][k]
#                         l2.append(min(l[k - 1], l[k], l[k + 1]) + b[j][k])
#                 l=l2
#
#
#             else:
#                 print(l[0])





