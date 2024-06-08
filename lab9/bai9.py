# Nhap vao mot so nguyen duong n
n = input("Nhap mot so nguyen duong: ")
# chuyen string => integer
n = int(n)
# kiem tra n > 0
while n < 0:
    print("Can nhap mot so nguyen lon hon 0.")
    n = int(input("Nhap mot so nguyen duong: "))

# tao danh sach chua diem
ds_diem = []

# cho nhap diem (0 => 10)
for i in range(n):
    # nhap diem (float)
    diem = float(input("Nhap diem bai kt: "))
    # kiem tra diem
    while not (0 <= diem <= 10):
        # bao loi
        print("Can nhap diem tu 0 => 10")
        diem = float(input("Nhap diem bai kt: "))
    # them diem vao danh sach
    ds_diem.append(diem)

# sap xep danh sach diem
ds_diem.sort(reverse=False)

# tim gia tri nho nhat trong danh sach
min = ds_diem[0]
while ds_diem.count(min) > 0:
    ds_diem.remove(min)

# in danh sach theo kieu string
# cach 1 --------------
print("Danh sach diem:", end=" ")
for i in ds_diem:
    print(i, end=" ")
print()
# cach 2 --------------
string = "Danh sach diem: " + " ".join([str(i) for i in ds_diem])
print(string)

# dem so diem >= 8
# cach 1
count = 0
for i in ds_diem:
    if i >= 8:
        count += 1
print("So luong diem tren 8:", count)
# cach 2
temp_list = [i for i in ds_diem if (i >= 8)]
print("so luong diem tren 8:", len(temp_list))
