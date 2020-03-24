x = [[12,7,3],
     [4 ,5,6],
     [1,3,4]]

y = [[5,8,1],
     [6,7,3],
     [2,5,3]]

def cek(x):
    for i in range(len(x)):
        if len(x[0])==len(x[i]):
            pass

        else:
            print('error')
            break

cek(x)

def tambah(x,y):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print(x[i][j] + y[i][j],end='   ')
        print()

def kali(x,y):
    a=[]
    for i in range(0, len(x)):
        row = []
        for j in range(0, len(x[0])):
            total = 0
            for z in range(0, len(x)):
                total = total + (x[i][z] * y[z][j])
            row.append(total)
        a.append(row)

    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            print (a[i][j], end='  ')
        print ()

kali(x,y)

def determinan(x):
        d=(x[0][0]*x[1][1])-(x[0][1]*x[1][0])
        print(d)

a=[[2,3],[4,5]]
determinan(a)
