def say_hello(name):
    print("Hello ban", name)


say_hello(name="ABC")


def sum(a, b):
    return a + b


print(sum(12.5, 2.3))


def tinh_tong_phan_so():
    # nhap du lieu
    phan_so_1 = input("nhap tu, mau cach nhau dau ,: ")
    phan_so_2 = input("nhap tu, mau cach nhau dau ,: ")

    # format du lieu
    phan_so_1 = phan_so_1.split(",")
    phan_so_2 = phan_so_2.split(",")

    # khai bao tu, mau 2 phan so
    tu_1 = int(phan_so_1[0])
    tu_2 = int(phan_so_2[0])
    mau_1 = int(phan_so_1[1])
    mau_2 = int(phan_so_2[1])

    # cong tu so (phai cung mau so)
    tong_tu = tu_1 * mau_2 + tu_2 * mau_1

    # cong mau so
    tong_mau = mau_1 * mau_2

    return str(tong_tu) + '/' +str(tong_mau)

print(tinh_tong_phan_so())

# chi dung khi can import cho file khac
# if __name__ == '__main__':
#     say_hello('ABC')
