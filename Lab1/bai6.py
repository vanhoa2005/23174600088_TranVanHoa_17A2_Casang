import math

def cong_vector(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def tru_vector(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def do_dai_vector(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)

def tich_vo_huong(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def cosin_goc(a, b):
    tich = tich_vo_huong(a, b)
    do_dai_a = do_dai_vector(a)
    do_dai_b = do_dai_vector(b)
    cosin = tich / (do_dai_a * do_dai_b)
    return round(cosin, 2)

# Nhập tọa độ của vector a và b
a = [float(x) for x in input("Nhập tọa độ của vector a (x, y, z): ").split()]
b = [float(x) for x in input("Nhập tọa độ của vector b (x, y, z): ").split()]

# Phép cộng và phép trừ vector
cong = cong_vector(a, b)
tru = tru_vector(a, b)

# Độ dài của vector a và b
do_dai_a = do_dai_vector(a)
do_dai_b = do_dai_vector(b)

# Cosin góc hợp giữa hai vector a và b
cos_goc = cosin_goc(a, b)

# In kết quả
print("1. Phép cộng vector a + b:", cong)
print("   Phép trừ vector a - b:", tru)
print("2. Độ dài của vector a:", round(do_dai_a, 2))
print("   Độ dài của vector b:", round(do_dai_b, 2))
print("3. Cosin góc hợp giữa hai vector a và b:", cos_goc)