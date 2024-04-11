'''Viết một chương trình Python để kiểm tra xem có thể thay đổi một chuỗi thành 
một chuỗi khác bằng cách thêm, xóa hoặc thay đổi một số ký tự trong chuỗi ban 
đầu hay không'''

chuoi_1 = input("Hãy nhập một chuỗi : ")
chuoi_2 = input("Hãy nhập một chuỗi : ")
bo_ky_tu_1 = set(chuoi_1)
bo_ky_tu_2 = set(chuoi_2)
if bo_ky_tu_2.issubset(bo_ky_tu_1):
  so_luong_can_them = len(chuoi_2) - len(chuoi_1)
  if so_luong_can_them >= 0:
    print(f"Có thể chuyển đổi '{chuoi_1}' thành '{chuoi_2}'")
  else:
    print(f"Không thể chuyển đổi '{chuoi_1}' thành '{chuoi_2}'")
else:
  print(f"Không thể chuyển đổi '{chuoi_1}' thành '{chuoi_2}'")