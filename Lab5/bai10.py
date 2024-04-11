'''Viết một chương trình Python để xóa tất cả các khoảng trắng giữa các ký tự
trong một chuỗi đã cho.'''

chuoi = "Vẻ bề ngoài quan trọng đến thế sao !"
chuoi_moi = ""
for ky_tu in chuoi:
  if ky_tu != " ":
    chuoi_moi += ky_tu
print(f"Chuỗi sau khi xóa khoảng trắng: {chuoi_moi}")
