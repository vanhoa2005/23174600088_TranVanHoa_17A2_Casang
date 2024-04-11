'''Bài 1:
Viết một chương trình Python nhận đầu vào là một số nguyên dương (số thập 
phân), và sau đó chuyển đổi nó sang số nhị phân.'''

so_nguyen_duong = int(input("Nhập số nguyên dương : "))
so_nhi_phan = " "
while so_nguyen_duong > 0:
  so_du = so_nguyen_duong % 2
  so_nhi_phan = str(so_du) + so_nhi_phan
  so_nguyen_duong //= 2
print(f"Số nhị phân của số vừa nhập là: {so_nhi_phan}")


