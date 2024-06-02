# in ra so chan tu 1 => n  (n >0)
# nhap bien n
n = int(input('Nhap so nguyen: '))
# kiem tra n > 0
if n <= 0:
    print('Loi: can nhap n > 0')
else:
    # chay vong lap tu 1 => n 
    for i in range(n + 1):
        # kiem tra i la so chan
        if i % 2 == 0:
            print(i, end=' ')
