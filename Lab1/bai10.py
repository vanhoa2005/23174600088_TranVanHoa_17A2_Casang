def tinh_xac_suat(tong_so_bi, so_bi_muon_rut, loai_bi_muon_rut):
    # Tính tổ hợp chập m từ n phần tử
    def tinh_combinations(n, m):
        numerator = 1
        denominator = 1
        for i in range(n, n - m, -1):
            numerator *= i
        for i in range(1, m + 1):
            denominator *= i
        return numerator / denominator
    
    # Tính xác suất
    xac_suat = tinh_combinations(tong_so_bi - so_bi_muon_rut, so_bi_muon_rut) / tinh_combinations(tong_so_bi, so_bi_muon_rut)
    
    return round(xac_suat, 4)

# Số lượng viên bi theo từng màu
tong_so_bi = 50
so_bi_do = 20
so_bi_xanh = 15
so_bi_vang = 15

# Nhập số lượng viên bi mà người dùng muốn rút ra
so_bi_muon_rut = int(input("Nhập số lượng viên bi bạn muốn rút ra: "))

# 1. Tất cả là bi đỏ
xac_suat_bi_do = tinh_xac_suat(tong_so_bi, so_bi_muon_rut, so_bi_do)
print("1. Xác suất để rút ra tất cả là bi đỏ:", xac_suat_bi_do)

# 2. Ít nhất một viên là bi xanh
xac_suat_bat_ky_bien_xanh = 1 - tinh_xac_suat(tong_so_bi, so_bi_muon_rut, so_bi_do)
print("2. Xác suất để rút ra ít nhất một viên là bi xanh:", round(xac_suat_bat_ky_bien_xanh, 4))

# 3. Đúng hai viên là bi vàng
xac_suat_hai_bi_vang = tinh_xac_suat(so_bi_vang, 2, 2)
print("3. Xác suất để rút ra đúng hai viên là bi vàng:", xac_suat_hai_bi_vang)