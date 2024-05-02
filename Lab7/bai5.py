kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

hoa_don = []
while True:
    mat_hang = input("Nhập tên mặt hàng (hoặc 'q' để thoát): ")
    if mat_hang.lower() == "q":
        break

    so_luong = int(input("Nhập số lượng: "))

    if mat_hang not in kho or so_luong > kho[mat_hang]:
        print(f"Số lượng {mat_hang} không đủ trong kho.")
        continue

    kho[mat_hang] -= so_luong

    thanh_tien = so_luong * gia_tien[mat_hang]

    hoa_don.append({
        "mat_hang": mat_hang,
        "so_luong": so_luong,
        "don_gia": gia_tien[mat_hang],
        "thanh_tien": thanh_tien
    })

tong_tien = 0
for item in hoa_don:
    print(f"{item['mat_hang']}: {item['so_luong']} x {item['don_gia']:.2f} = {item['thanh_tien']:.2f}")
    tong_tien += item["thanh_tien"]

print(f"Tổng tiền: {tong_tien:.2f}")

for mat_hang, so_luong in kho.items():
    print(f"{mat_hang}: {so_luong}")
