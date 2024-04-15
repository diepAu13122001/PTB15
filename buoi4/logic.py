# boolean ------------------------------
# bieu thuc logic
m = 4 != 4  # 4 khong bang 4 => false
n = 3 == 3  # 3 bang voi 3 => true
o = 3 >= 2  # 3 lon hon hoac bang 2 => true
p = 12 <= 16  # 12 nho hon hoac bang 16 => true
print(m, n, o, p)

# phep toan bieu thuc logic
# and: va (true + true => true)
# or: hoac (true + ... => true)
# not: phu dinh
print(m and o)
# false and true => false
print((p or m) and (not o))
# true or false => true
# not o => false
# true and false => false
print(n or (not p))
# true or false => true
print(((n and (not m)) and p) or o)
# n and (not m) => true and true => true
# true and true => true
# true or true => true