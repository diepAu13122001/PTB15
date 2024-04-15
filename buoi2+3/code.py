# Khai bao bien so --------------------------------
age = 25

# Nguoi dung nhap 1 so tuoi => tinh tuoi 10 nam sau
# Kieu du lieu -------------------------------------
# integer (so nguyen) + float (so thuc/ so thap phan)
x, y, z = 10, 10.5, -3
print(type(x)) # class int
print(type(y)) # class float
print(type(z)) # class int
#  phep toan cho kieu so (int, float)
result = x + y * z / x - 12
mu = x**2 # mu cua x (10**2 = 10 * 10)
chia_lay_nguyen = x // z
chia_lay_du = x % 2 
print(mu)
print(chia_lay_nguyen)
print(chia_lay_du)
# kieu string (chuoi)
first_name = "Au"
last_name = "Diep"
name = first_name + " " + last_name
print(type(name)) # class str
# kieu boolean (true/ false)
female = True
print(type(female)) # class bool
m = 12 < 5 or 4 > 0 # bieu thuc logic (and, or, not)
print(m) # True

# type casting (convert type) -----------------------
user_input = input("Nhap mot so: ") # bat buoc terminal
# doi tu str => int
user_input = int(user_input)
print(type(user_input))
# doi tu str => float 
user_input = float(user_input)
print(type(user_input))
# doi float/ int => str
num = 123.5
num = str(num)
print(type(num))
# khong the dung toan tu cho 2 kieu du lieu khac nhau
# print(num + False) 








