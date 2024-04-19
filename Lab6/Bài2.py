'''Viết một chương trình Python để thực hiện các thao tác sau:
+ Cho phép người dùng nhập vào một mảng gồm n số nguyên dương từ bàn 
phím.
+ Tìm và in ra màn hình tất cả các số nguyên tố trong mảng đó.
+ Tìm và in ra màn hình tất cả các số hoàn hảo trong mảng đó.'''
n = int(input("Nhập số lượng phần tử: "))
mang_so_nguyen = []

for i in range(n):
  so_nguyen = int(input(f"Nhập phần tử thứ {i + 1}: "))
  mang_so_nguyen.append(so_nguyen)

# In các số nguyên tố
print("Các số nguyên tố trong mảng:")
for so_nguyen in mang_so_nguyen:
  check = True
  for j in range(2, int(so_nguyen**0.5) + 1):
    if so_nguyen % j == 0:
      check = False
      break
  if check:
    print(so_nguyen, end=" ")

# In các số hoàn hảo
print("Các số hoàn hảo trong mảng:")
for so_nguyen in mang_so_nguyen:
  so_hoan_hao = 0
  for i in range(1, int(so_nguyen**0.5) + 1):
    if so_nguyen % i == 0:
      so_hoan_hao += i
      if n // i != i:
        so_hoan_hao += n // i
  if so_hoan_hao == so_nguyen:
    print(so_hoan_hao, end=" ")




    