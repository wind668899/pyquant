# import math
#
#
# def ss(x):
#     for i in range(2,int(math.sqrt(x))+1):
#         #print(i)
#         if(x%i==0):
#             #print("false")
#             return 0
#     return  1
#
# a=input()
# b=list(map(int,input().split(' ')))
# x=[]
# y=[]
# data=[]
# for i in b:
#     if i%2==0:
#         x.append(i)
#     else:
#         y.append(i)
# print(x)
# print(y)
# for i in y:
#     m=[]
#     for j in x:
#         m.append(ss(i+j))
#     data.append(m)
# print(data)

# def check(a, b):
#     if a == b:
#         return False
#     if len(a) != len(b):
#         return False
#     la = list(a)
#     la.sort()
#     lb = list(b)
#     lb.sort()
#
#     if la != lb:
#         return False
#     return True
#
#
# a = input()
# b = a.split(' ')
# x = b[len(b) - 2]
# k = int(b[len(b) - 1])
# j = 0
# data = []
# for i in range(1, len(b) - 2):
#     if check(b[i], x):
#         j = j + 1
#         data.append(b[i])
# data.sort()
# if len(data) < k:
#     print(j)
# else:
#     print(j)
#     print(data[k - 1])
#
# a=[1, 2, 3, 8, 5, 11, 7, 8, 9, 10]
# a.sort(reverse=True)
# print(a)

# def check(a):
#     b = list(a)
#     for i in range(len(b) - 5):
#         b[i]
#         b[i + 1]
#         for j in range(i + 2, len(b) - 2):
#             if b[i] == b[j] and b[i + 1] == b[j + 1] and b[i + 2] == b[j + 2]:
#                 return False
#     return True
#
# while True:
#     try:
#         a = input()
#         x1 = 0
#         x2 = 0
#         x3 = 0
#         x4 = 0
#         K = True
#         for i in a:
#             if i == ' ' or i == '\n':
#                 K = False
#                 break
#             if i.isupper():
#                 x1 = 1
#             elif i.islower():
#                 x2 = 1
#             elif i.isdigit():
#                 x3 = 1
#             else:
#                 x4 = 1
#
#         if x1 + x2 + x3 + x4 > 2 and len(a) > 8 and K == True and check(a):
#             print('OK')
#         else:
#             print('NG')
#     except:
#         break
# print( int(5.9))

# def change(data):
#     a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#          'w', 'x', 'y', 'z', 'a']
#     for i in range(len(a) - 1):
#         if data == a[i]:
#             return a[i + 1]
#     return 0
#
#
# def check(i):
#     if i.islower():
#         if 'abc'.find(i) != -1:
#             return 2
#         if 'def'.find(i) != -1:
#             return 3
#         if 'ghi'.find(i) != -1:
#             return 4
#         if 'jkl'.find(i) != -1:
#             return 5
#         if 'mno'.find(i) != -1:
#             return 6
#         if 'pqrs'.find(i) != -1:
#             return 7
#         if 'tuv'.find(i) != -1:
#             return 8
#         if 'wxyz'.find(i) != -1:
#             return 9
#     elif i.isupper():
#         return change(i.lower())
#     else:
#         return i
#
#
# while 1:
#     try:
#         a = input()
#         for i in a:
#             print(check(i), end='')
#     except:
#         break

# while 1:
#     try:
#         x = int(input())
#         y = int(input())
#         z = int(input())
#         a = []
#         b = []
#         t = []
#         t1 = 0
#         h = []
#         for i in range(x):
#
#             k1=list(map(int, input().split(' ')))
#             #print(k1)
#             a.append(k1)
#         for i in range(y):
#             k1 = list(map(int, input().split(' ')))
#             #print(k1)
#             b.append(k1)
#             #b.append(list(map(int, input())))
#         #print(a)
#         #print(b)
#         for i in range(x):
#             for m in range(z):
#                 for j in range(y):
#                     t1 = t1 + a[i][j] * b[j][m]
#                 h.append(t1)
#                 t1=0
#             t.append(h)
#             h=[]
#         #print('11111111111')
#         #print(t)
#         for i in t:
#             for j in i:
#                 print(j, end=' ')
#             print()
#
#     except:
#         #print(222)
#         break
#
# while 1:
#     try:
#         a=int(input())
#         b=int(input())
#         d=[]
#         for i in range(a):
#             str=input()
#             x=str.split(' ')[0]
#             y=int(str.split(' ')[1])
#             d.append([x,y])
#         #print(d)
#         if b==0:
#             d.sort(key=,reverse=True)
#         else:
#             d.sort(key=lambda x:x[1])
#         #print(d)
#         for i in d:
#             print(i[0],end=' ')
#             print(i[1])
#             #print(str(i[0])+' '+str(i[1]))
#     except:
#         break

# a=input()
# x=1
# for i in a:
#     if x % 8 == 0:
#         print(i)
#     else:
#         print(i, end='')
#     x = x + 1

# tinydict = {'a': 1, 'b': 2}
# for i in tinydict:
#     print(i)
print(chr(ord('a')+1))
