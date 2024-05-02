'''Viết chương trình sử dụng kiến thức về từ điển nhập từ bàn phím thông tin của 
10 sinh viên, bao gồm: tên và điểm thi. Yêu cầu: 
1. Xếp loại học lực của sinh viên theo điểm thi:
+ Điểm dưới 4.0: F
+ Điểm từ 4.0 đến 5.4: D
+ Điểm từ 5.5 đến 6.9: C
+ Điểm từ 7.0 đến 8.4: B
+ Điểm từ 8.5 đến 10.0: A
2. Thống kê số lượng sinh viên ở mỗi loại học lực.'''


# Khởi tạo từ điển để lưu thông tin của sinh viên
sinh_vien = {}

# Nhập thông tin của 10 sinh viên
for i in range(1, 11):
    ten = input(f"Nhập tên của sinh viên {i}: ")
    diem = float(input(f"Nhập điểm của sinh viên {i}: "))
    sinh_vien[ten] = diem

# Tạo từ điển để lưu số lượng sinh viên ở mỗi loại học lực
thong_ke = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

# Tính loại điểm và thống kê số lượng sinh viên ở mỗi loại học lực
for ten, diem in sinh_vien.items():
    if diem < 4.0:
        thong_ke['F'] += 1
    elif 4.0 <= diem < 5.5:
        thong_ke['D'] += 1
    elif 5.5 <= diem < 7.0:
        thong_ke['C'] += 1
    elif 7.0 <= diem < 8.5:
        thong_ke['B'] += 1
    else:
        thong_ke['A'] += 1

# Hiển thị kết quả
print("Kết quả thống kê số lượng sinh viên theo loại học lực:")
for loai_diem, so_luong in thong_ke.items():
    print(f"Loại {loai_diem}: {so_luong} sinh viên")
