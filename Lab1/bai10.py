hop = 50
bi_do = 20
bi_xanh = 15
bi_vang = 15
from math import factorial
tat_ca_bi_do = factorial(20) / factorial(20) * factorial(20-20)
khong_gian_mau = tat_ca_bi_do/(factorial(50)/factorial(20)*factorial(50-20))
xac_suat = tat_ca_bi_do/khong_gian_mau
print("Xác suất để lấy ra tất cả là bi màu đỏ là : ",xac_suat)