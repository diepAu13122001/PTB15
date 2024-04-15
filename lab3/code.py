# bai 9 --------------------------------
# nhap vao so keo
m = input("Nhap so keo: ")
#  chuyen m => int
m = int(m)
# nhap vao so hoc sinh
n = input("Nhap so hoc sinh: ")
#  chuyen n => int
n = int(n)
# xuat ra so keo moi ban nhan duoc
print("So keo moi ban nhan duoc: ", m // n)
# xuat ra so keo con lai
print("So keo con lai: ", m % n)

# bai 10 --------------------------------
# int: integer: so nguyen
# float: so thap phan
# Nhap vao so nguyen giay
sec = int(input("So giay"))
# cal hour
hour = sec // 3600
# cal min
min = (sec % 3600) // 60
# cal sec
sec = sec - (hour * 3600 + min * 60)
# in ket qua
print(f"{hour} gio {min} phut {sec} giay")
