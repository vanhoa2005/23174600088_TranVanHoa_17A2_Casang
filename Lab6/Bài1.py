'''Viết một chương trình Python để thực hiện các thao tác sau:
+ Cho phép người dùng nhập vào một mảng gồm n số nguyên dương từ bàn 
phím.
+ Phân loại và tính tổng:
Tính tổng của tất cả các số chẵn trong mảng.
Tính tổng của tất cả các số lẻ trong mảng.
Xuất hai kết quả trên ra màn hình.'''


mang_so_nguyen = []
tong_chan = 0
tong_le = 0
n = int(input("Nhập số lượng phần tử: "))

for i in range(n):
  so_nguyen = int(input(f"Nhập phần tử thứ {i + 1}: "))
  mang_so_nguyen.append(so_nguyen)

for so in mang_so_nguyen:
  if so % 2 == 0:
    tong_chan += so
for so in mang_so_nguyen:
  if so % 2 != 0:
    tong_le += so

print(f"Mảng số nguyên đã nhập: {mang_so_nguyen}")
print(f"Tổng của tất cả các số chẵn trong mảng: {tong_chan}")
print(f"Tổng của tất cả các số chẵn trong mảng: {tong_le}")
