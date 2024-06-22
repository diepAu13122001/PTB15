# nhap chuoi diem
s = input('Nhap chuoi diem cach nhau boi dau " " : ')
# cat chuoi => danh sach diem
s = s.split(' ')
# kiem tra so luong diem 10
if '10' in s:
    print('So luong diem 10: ', s.count('10'))
else:
    print('Ban chua co diem 10')

