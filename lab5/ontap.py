# Bai 1: Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình
# khai bao bien inp => gan bien => chuyen kieu du lieu
# inp = int(input("Nhap so: "))
# # thay doi gia tri bien
# inp = (inp * 3) + 1
# # in ket qua ra man hinh
# print(inp)


# Bai 2: Nhập vào số n, hãy mũ 2 rồi chia cho 3, sau đó in kết quả ra màn hình
# inp = int(input("Nhap so: "))
# # thay doi gia tri bien
# inp = (inp**10) / 3
# print(inp)

# Bai 3: Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False
# inp = int(input("Nhap so: "))
# if inp % 2 == 0:
#     print(True)
# else:
#     print(False)

# Bai 4: Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
# a = int(input("Nhap so: "))
# if a % 3 == 0 and 50 <= a <= 100:
#     print(True)
# else:
#     print(False)
# # viet tat
# print(True) if a % 3 == 0 and 50 <= a <= 100 else print(False)

# Bài 5: Nhập vào số nguyên a, nếu a là số chia hết cho 5
# nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
a = int(input("Nhap so: "))
if a % 5 == 0 and not (20 <= a <= 70):
    print(True)
else:
    print(False)
