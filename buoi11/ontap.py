# vong for --------------------------------------------------------
# In các số chẵn chia hết cho 3 bé hơn 100
print("Bai1--------------------")
for i in range(100):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")

# vong while ------------------------------------------------------
# Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.
# Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập
print("Bai2--------------------")
n = int(input("Nhap so: "))
num_max = n
num_min = n
while n != -1:
    n = int(input("Nhap tiep: "))
    if n != -1:
        num_max = max(n, num_max)
        if num_min > n:
            num_min = n
print("So lon nhat:", num_max)
print("So nho nhat:", num_min)

# danh sach -------------------------------------------------------
# L = [-1,6,-4,8,10,-1,2] (6), tìm và in ra giá trị dương đầu tiên của list,
# nếu không có giá trị dương, ta in ra -1 (break)
print("Bai3--------------------")
L1 = [-1, 6, -4, 8, 10, -1, 2]
L2 = [-10, -6, -4, -8, -10, -1, -2]
print("for L1: ")
isOut = False
for i in L1:
    if i > 0:
        print("Gia tri dau tien > 0:", i)
        isOut = True
        break

if isOut == False:
    print("Khong co gia tri nao >0", -1)

print("for L2: ")
isOut = False
for i in L2:
    if i > 0:
        print("Gia tri dau tien lon hon 0:", i)
        isOut = True
        break
if isOut == False:
    print("Khong co gia tri nao >0:", -1)
