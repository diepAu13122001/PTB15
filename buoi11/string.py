# Duyet phan tu trong string -----------------------------
s = "MindX Technology School"
# cach 1 (su dung index)
for i in range(len(s)):
    print(s[i])

# cach 2
for character in s:
    print(character)

# Substring (xau con) ---------------------------------------
a = "abcd"
b = "b"
z = "z"
# kiem tra b co trong a khong (contain)
# find - tra ve vi tri cua phan tu
print(a.find(b))  # 1
print(a.find(z))  # -1
# find(<xau con>, <start>, <stop>)
print(a.find("d", 0, 2))  # -1
# toan tu in
print(b in a)  # true
print(z in a)  # false

# Ham ho tro khi thao tac voi string ----------------------------
# split(<ky tu cach>) - cat chuoi thanh danh sach
# Bai toan: nhap day so nguyen cach nhau = dau ' ' 
# => in ra max
l = input('Nhap danh sach so nguyen: ')
lis = l.split(' ')
print(lis)
print(max(lis))

# replace (<gia tri cu>, <gia tri moi>, <so luong gia tri muon thay>) 
# thay gia tri cu => gt moi
# Bai toan: chinh lai url cho dung ('\\')
url = input('Nhap url: ')
while '/' in url:
    url = url.replace('/', '\\\\')
print('Url chinh xac: ' + url)
