#
S1 = 0
n = int(input("Nhập n (n > 10): "))
a = 1
while a <= n:
    S1 += 6**a
    a += 1
print(f"a)Tổng S1 = {S1}")

#
n = int(input("Nhập n: "))
a = 0
S2 = 0
while a <= n:
    S2 += 1 / 3**(2*a + 1)
    a += 1
print(f"b)Tổng S2 = {S2}")

#
n = int(input("Nhập n: "))
a = 1
S3 = 0
while a <= n:
    S3 += (-1)**a * a**2
    a += 1
print(f"c)Tổng S3 = {S3}")

#
n = int(input("Nhập n: "))
a = 1
S4 = 0
while a <= n:
    S4 += a*(a+1)*(a+2)
    a += 1
print(f"d)Tổng S3 = {S4}")




