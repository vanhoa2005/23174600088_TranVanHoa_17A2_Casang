'''
Viết chương trình yêu cầu người dùng nhập một chuỗi văn bản và từ cần tìm 
kiếm. Sau đó, hiển thị vị trí (index) của từ đó trong chuỗi và kiểm tra xem từ
nào xuất hiện nhiều nhất trong chuỗi sau đó hiển thị kết quả.
'''

chuoi = input("Nhập chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm kiếm: ")
vi_tri = chuoi.find(tu_can_tim)
so_lan_xuat_hien = 0
while vi_tri != -1:
  so_lan_xuat_hien += 1
  vi_tri = chuoi.find(tu_can_tim, vi_tri + len(tu_can_tim))
print(f"Vị trí đầu tiên của từ '{tu_can_tim}' trong chuỗi là: {vi_tri}")
print(f"Số lần xuất hiện của từ '{tu_can_tim}' trong chuỗi là: {so_lan_xuat_hien}")
danh_sach_tu = chuoi.split()
so_lan_xuat_hien_dict = {}
for tu in danh_sach_tu:
  vi_tri = chuoi.find(tu)
  so_lan_xuat_hien = 0
  while vi_tri != -1:
    so_lan_xuat_hien += 1
    vi_tri = chuoi.find(tu, vi_tri + len(tu))
  so_lan_xuat_hien_dict[tu] = so_lan_xuat_hien
tu_xuat_hien_nhieu_nhat = max(so_lan_xuat_hien_dict, key=so_lan_xuat_hien_dict.get)
print(f"Từ xuất hiện nhiều nhất trong chuỗi là: '{tu_xuat_hien_nhieu_nhat}' với {so_lan_xuat_hien_dict[tu_xuat_hien_nhieu_nhat]} lần xuất hiện")
