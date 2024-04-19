n = int(input("Nhập kích thước ma trận vuông: "))
ma_tran = []
for i in range(n):
  dong = []
  for j in range(n):
    dong.append(float(input(f"Nhập phần tử [{i+1},{j+1}]: ")))
  ma_tran.append(dong)

print("Ma trận đã nhập:")
for dong in ma_tran:
  print(dong)
