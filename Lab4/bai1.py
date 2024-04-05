'''Bài 1:
Viết chương trình nhập vào các số nguyên dương từ bàn phím cho đến khi tổng 
các số đã nhập vượt quá 1000. Sau đó in ra màn hình:
a) Các số lẻ đã nhập
b) Các số chẵn đã nhập
c) Đếm số lượng số nguyên đã nhập'''

tong = 0
so_luong = 0
so_le = ' '
so_chan = ' '
while tong <= 1000:
  so = int(input("Nhập số nguyên dương: "))
  tong += so
  so_luong += 1
  if so % 2 == 0:
    so_chan += str(so) + ' '
  else:
    so_le += str(so) + ' '
print("a) Các số lẻ đã vừa nhập:", so_le)
print("b) Các số chẵn đã vừa nhập:", so_chan)
print("c) Số lượng số nguyên đã nhập:", so_luong)















