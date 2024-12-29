# while 1:
#     try:
#         a=list(map(int,input().split(' ')))
#         t=set()
#         i=0
#         j=0
#         k=0
#         lenth=len(a)
#         while 1:
#
#             if lenth-k==1 and a[i+j] not in t:
#                 print(a[i+j])
#                 break
#             if a[i+j] in t:
#                 j=j+1
#                 continue
#             if (i+1) % 3 == 0:
#                 t.add(a[i + j])
#                 a.extend(a)
#                 k = k + 1
#             i=i+1
#     except:
#         break



while True:
    try:
        a=input()
        b=set()
        c=[]
        for i in a:
            if i not in b:
                c.append(i)
                b.add(i)
        c.sort()
        for i in c:
            print(i,end='')
    except:
        break
