a = [3, 7, 35, 20, 47, 88, 106, 92, 120, 11]
b = [13, 5, 19, 17, 2, 8, 45, 18, 29, 63, 25, 40]

def Array_1(a,b):
    c = a + b
    for i in range(1,len(c)):
        nilai = c[i]
        pos = i
        while pos >0 and nilai<c[pos - 1]:
            c[pos]= c[pos-1]
            pos -= 1
        c[pos] = nilai
    print(c)

def Array_2(a,b):
    ad0 = len(a)
    ad1 = len(b)
    x= 0
    y=0
    c = []
    while x < ad0 and y < ad1:
        if a[x]<b[y]:
            c.append(a[x])
            x += 1
        else:
            c.append(b[y])
            y += 1
    while x<ad0:
        c.append(a[x])
        x += 1
    while y<ad1:
        c.append(b[y])
        y += 1
    return c
