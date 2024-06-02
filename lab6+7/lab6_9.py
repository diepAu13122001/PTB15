# tinh tong tu 1 => n (n la so nguyen > 0, ng dung nhap vao)
# nhap so nguyen
n = int(input("Nhap so nguyen: "))
# Kiem tra so nguyen > 0
if n > 0:
    # chay vong lap 1 => n
    sum = 0  # khai bao bien cho phan tong
    for i in range(n+1):
        # tinh tong
        sum += i
    # in ket qua
    print("Tong tu 1 den " + str(n) + " la: " + str(sum))
else:
    print("Loi: can nhap mot so lon hon 0")
