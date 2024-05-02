van_ban = input("Nhập văn bản: ")

tu_dien = {}
for tu in van_ban.split():
  tu = tu.lower()
  tu_dien[tu] = tu_dien.get(tu, 0) + 1

tu_nhieu_nhat = max(tu_dien, key=tu_dien.get)
so_luong_nhieu_nhat = tu_dien[tu_nhieu_nhat]

tu_it_nhat = min(tu_dien, key=tu_dien.get)
so_luong_it_nhat = tu_dien[tu_it_nhat]

print(f"Từ xuất hiện nhiều nhất: {tu_nhieu_nhat} ({so_luong_nhieu_nhat} lần)")
print(f"Từ xuất hiện ít nhất: {tu_it_nhat} ({so_luong_it_nhat} lần)")
   