# Nhap 2 so nguyen a, b, tinh tong cac so chan
# trong khoang a => b. In ra man hinh tong.
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

s = 0

if a == b:
    print("Khong duoc trung 2 so")
else:
    for i in range(a, b):
        if i % 2 == 0:
            s += i  # s = s + i
    print("Tong so chan trong day la: " + str(s))

