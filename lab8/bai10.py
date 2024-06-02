A = [1, 8, 9, 10, -1]

# khai bao bien luu max, min (gia tri: phan tu dau tien cua ds)
max = A[0]
min = A[0]

for i in A:
    if i > max:
        max = i
    if i < min:
        min = i

print('Max', max)
print('Min', min)
