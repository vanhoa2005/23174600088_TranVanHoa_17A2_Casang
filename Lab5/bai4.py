'''Viết một chương trình Python để loại bỏ tất cả các ký tự không phải là số khỏi 
một chuỗi ký tự đã cho. Sau đó, kiểm tra xem chuỗi ký tự kết quả có phải là một 
số nguyên tố không và hiển thị kết quả cho người dùng'''

ky_tu_so = "0123456789"
chuoi = input("Nhập chuỗi ký tự: ")
chuoi_so = ""
for char in chuoi:
  if char in ky_tu_so:
    chuoi_so += char
if chuoi_so == "":
  print("Chuỗi không chứa số nào!")
  exit()
so = int(chuoi_so)
nguyen_to = True
if so <= 1:
  nguyen_to = False
else:
  for i in range(2, int(so**0.5) + 1):
    if so % i == 0:
      nguyen_to = False
      break
if nguyen_to:
  print(f"{so} là số nguyên tố.")
else:
  print(f"{so} không phải là số nguyên tố.")
