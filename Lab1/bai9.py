def tinh_trung_diem(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

# Nhập tọa độ của các đỉnh từ người dùng
M = tuple(map(float, input("Nhập tọa độ của điểm M (x, y): ").split()))
N = tuple(map(float, input("Nhập tọa độ của điểm N (x, y): ").split()))
P = tuple(map(float, input("Nhập tọa độ của điểm P (x, y): ").split()))
Q = tuple(map(float, input("Nhập tọa độ của điểm Q (x, y): ").split()))

# Tính toán tọa độ trung điểm của các cạnh
Diem_trung_MN = tinh_trung_diem(M, N)
Diem_trung_NP = tinh_trung_diem(N, P)
Diem_trung_PQ = tinh_trung_diem(P, Q)
Diem_trung_QM = tinh_trung_diem(Q, M)

# In kết quả
print("Tọa độ trung điểm của cạnh MN:", Diem_trung_MN)
print("Tọa độ trung điểm của cạnh NP:", Diem_trung_NP)
print("Tọa độ trung điểm của cạnh PQ:", Diem_trung_PQ)
print("Tọa độ trung điểm của cạnh QM:", Diem_trung_QM)