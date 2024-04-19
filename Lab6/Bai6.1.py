'''Viết một chương trình Python để thực hiện các thao tác sau trên ma trận:
Bài 6.1:
+ Nhập Ma trận: Cho phép người dùng nhập các phần tử của một ma trận có 
kích thước m x n từ bàn phím.
+ Tổng của Ma trận: Tính tổng của tất cả các phần tử trong ma trận.
+ Tích của Ma trận: Cho phép nhập một ma trận thứ hai và tính tích của hai ma 
trận (nếu có thể).
+ Ma trận chuyển vị: Tạo và in ra ma trận chuyển vị của ma trận ban đầu.
Bài 6.2:
+ Nhập ma trận vuông: Cho phép người dùng nhập các phần tử của một ma 
trận vuông từ bàn phím.
+ Tìm ma trận nghịch đảo: Tìm và xuất ra màn hình ma trận nghịch đảo của ma 
trận đã nhập (nếu tồn tại).
+ Kiểm tra xem ma trận đã cho có phải là ma trận đối xứng hay không.'''


m = int(input("Nhập số hàng ma trận 1: "))
n = int(input("Nhập số cột ma trận 1: "))
ma_tran = []
for i in range(m):
  hang = []
  for j in range(n):
    phan_tu = float(input(f"Nhập phần tử [{i},{j}]: "))
    hang.append(phan_tu)
  ma_tran.append(hang)


# In ma trận ra màn hình
for i in range(m):
  for j in range(n):
    print(f"{ma_tran[i][j]:.2f}", end=" ")
  print()
# Tính tổng của ma trận
tong = 0
for i in range(m):
  for j in range(n):
    tong += ma_tran[i][j]

# In tổng ra màn hình
print("Tổng của ma trận 1:", tong)





m2 = int(input("Nhập số hàng ma trận 2: "))
n2 = int(input("Nhập số cột ma trận 2: "))
ma_tran2 = []
for i in range(m2):
  hang2 = []
  for j in range(n2):
    phan_tu2 = float(input(f"Nhập phần tử [{i},{j}]: "))
    hang2.append(phan_tu2)
  ma_tran2.append(hang2)


# In ma trận ra màn hình
for i in range(m2):
  for j in range(n2):
    print(f"{ma_tran2[i][j]:.2f}", end=" ")
  print()
# Tính tổng của ma trận
tong2 = 0
for i in range(m2):
  for j in range(n2):
    tong2 += ma_tran2[i][j]

# In tổng ra màn hình
print("Tổng của ma trận 2:", tong2)





tich = [[0 for _ in range(n2)] for _ in range(m)]
for i in range(m):
  for j in range(n2):
    for k in range(n):
      tich[i][j] += ma_tran[i][k] * ma_tran2[k][j]
print("Tích của 2 ma trận là : ",tich)



# Tạo ma trận chuyển vị
ma_tran_chuyen_vi = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
  for j in range(n):
    ma_tran_chuyen_vi[j][i] = ma_tran[i][j]

# In ma trận chuyển vị ra màn hình
print("Ma trận chuyển vị của m trận ban đầu là :")
for i in range(n):
  for j in range(m):
    print(f"{ma_tran_chuyen_vi[i][j]:.2f}", end=" ")
  print()


