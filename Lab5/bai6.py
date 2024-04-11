'''Viết một chương trình Python nhập một chuỗi từ bàn phím và thực hiện các 
yêu cầu sau:
+ Kiểm tra xem mỗi ký tự trong chuỗi có phải là một ký tự đặc biệt (không phải 
ký tự chữ hoặc số) không.
+ Nếu có, đếm số lần xuất hiện của từng ký tự đặc biệt trong chuỗi.
+ Tính tỷ lệ phần trăm của mỗi ký tự đặc biệt trong chuỗi so với tổng số ký tự
trong chuỗi.'''


chuoi = input("Hãy nhập chuỗi các ký tự : ")
dem_ky_tu_dac_biet = {}
tong_so_ky_tu = len(chuoi)

for ky_tu in chuoi:
  if not ky_tu.isalpha() and not ky_tu.isdigit():
    if ky_tu not in dem_ky_tu_dac_biet:
      dem_ky_tu_dac_biet[ky_tu]=0
    dem_ky_tu_dac_biet[ky_tu] += 1

for ky_tu, so_lan_xuat_hien in dem_ky_tu_dac_biet.items():
  print(f"Ký tự '{ky_tu}' xuất hiện {so_lan_xuat_hien} lần")
  print(f"Tỷ lệ phần trăm: {so_lan_xuat_hien / tong_so_ky_tu * 100}%")



