def buatnol(x,y):
    a=[[0 for i in range(x)] for j in range(y)]
    print("array: ",a)
    print("matrik:")
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end='   ')
        print()


def buatnol2(x):
    a=[[0 for i in range(x)] for j in range(x)]
    print("array: ",a)
    print("matrik:")
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end='   ')
        print()


def identitas(x):
    a=[[1 if j==i else 0 for i in range(x)] for j in range(x)]
    print(a)
    print("============")
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end='   ')
        print()

identitas(5)
