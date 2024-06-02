# tinh tong tu 1 => x sao cho tong > n
# nhap n
n = int(input("Nhap 1 so nguyen"))
# khai bao bien tong
sum = 0
# khai bao bien dem x
x = 0
# kiem tra sum > n?
while n > sum:
    # tinh tong sum
    sum += x
    # in day so
    print(x, end=' ')
    # tang bien dem
    x += 1
