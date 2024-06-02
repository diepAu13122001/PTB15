n = 10
while n > 1:
    n -= 1
    print(n)

# Nhap bang cuu chuong
n = 0
while n == 0:
    n = int(input('Nhap so 2 - 9: '))
    if n == -1: 
        break
    if n > 9 or n < 2:
        n = 0
    else:
        for i in range (1, 10):
            print(str(i) + " x " + str(n) + " = "+ str(i*n))
        n = 0
