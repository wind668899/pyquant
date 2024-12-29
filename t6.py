#刘银辉 15817424993

def result(a):
    max = 0
    for i in range(len(a)):
        if i + 1 < len(a):
            for j in range(i + 1, len(a)):
                x = j - i
                y = min(a[i], a[j])
                if max < x * y:
                    max = x * y



    print(max)
a=[1,8,6,2,5,4,8,3,7]
result(a)



