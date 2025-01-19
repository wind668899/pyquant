# import math
#
#
# def ss(x):
#     for i in range(2,int(math.sqrt(x))+1):
#         print(i)
#         if(x%i==0):
#             print("false")
#             return 0
#     return  1
# a=input()
# print(ss(int(a)))

# for i in range(1,9):
#     print(i)

#


# a=set([1,2,3,4,5,5,5,3,4,])
# print(list(a))
# a=1
# if a in [1,2,3,4,5,5,5,3,4,]:
#     print(a)
# for k in [1,2,3,4,5,5,5,3,4,]:  # 从里面选择一个
#     print(k)
# a=7
# print(a//3)
# print(int(a/3))
# print(a%3)

#https://www.nowcoder.com/practice/78a1a4ebe8a34c93aac006c44f6bf8a1?tpId=37&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei&difficulty=&judgeStatus=&tags=&title=&sourceUrl=&gioEnter=menu
#数独
# def trueOrFalse(a,i,j):
#     for x in range(9):
#         if a[i][j]==a[x][j] and i!=x:
#             return False
#     for y in range(9):
#         if a[i][j] == a[i][y] and j != y:
#             return False
#     x=int(i/3)
#     y=int(j/3)
#     for m in range(3):
#         for n in range(3):
#             if a[i][j]==a[x*3+m][y*3+n] and (x*3+m!=i or y*3+n!=j):
#                 return  False
#     return True
#
#
#
# def checked(a):
#     for i in range(9):
#         for j in range(9):
#             if a[i][j]==0:
#                 for k in range(1,10):
#                     a[i][j]=k
#                     if trueOrFalse(a,i,j) and checked(a):
#                         return True
#                     a[i][j]=0
#                 return  False
#     return True
#
# a=list()
# for i in range(9):
#     b=list(map(int,input().split(' ')))
#     a.append(b)
# checked(a)
#
# for i in range(9):
#     for j in range(9):
#         print(a[i][j],end=' ')
#     print()
# for i in range(1,9):
#     print(i)
for i in range(2, 10):
    print(i)
# print(type(round(1.999999,0)))