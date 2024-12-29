# a=input()
# b=''
# #b=a.replace('(','').replace(')','').replace('<','').replace('>','')
# for i in range(len(a)):
#     if i==0 and a[i]!='('and a[i]!=')' and a[i]!='<' and a[i]!='>':
#         print(a[i], end='')
#         b=b+a[i]
#     elif a[i]!='('and a[i]!=')' and a[i]!='<' and a[i]!='>' and a[i-1]!='(' and a[i-1]!='<':
#         print(a[i], end='')
#         b=
#     elif a[i-1]=='<':
#          b=int(a[i])
#          for j in range(b):
#             print(a[i-2],end='')

x=int(input())
b=[]
for i in range(x):
    a=input().replace(' ','')
    k=True
    for j in range(len(a)):
        if j==0:
            if a[j].islower()==False:
                if a[j].isupper() ==True:
                    continue
                else:
                    k=False
                    break
        elif a[j].isdigit()==False:
            k=False
            break
    if k==True:
        c=''
        if len(a)!=9:
            c=a[0].lower()
            for j in range(9-len(a)):
                c=c+'0'
            for j in range(1,len(a)):
                c=c+a[j]
            b.append(c)
        else:
            b.append(a)
b.sort()
for i in range(len(b)):
    if i==0:
        print(b[i])
    elif b[i-1]==b[i]:
        continue
    else:
        print(b[i])




