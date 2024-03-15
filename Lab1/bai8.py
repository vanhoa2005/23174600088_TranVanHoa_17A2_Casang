x = float(input("Hãy nhập số thực x : "))
y = float(input("Hãy nhập số thực y : "))
z = float(input("Hãy nhập số thực z : "))
from math import sin,abs,log,atan,e
f = ((x**2 * sin(z) + abs(x) * 0.5) / log(z) + e**x-1 ) + atan(x*z)
print(f)
