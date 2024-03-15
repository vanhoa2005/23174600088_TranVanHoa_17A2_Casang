from math import *
x = float(input("Nhập giá trị của x: "))
z = float(input("Nhập giá trị của z: "))
print("f(x) =",round((((x**2)*sin(z)+abs(x)**0.5)/(log(z)+e**(x-1)))- atan(z*x),2))