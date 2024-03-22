'''Viết chương trình Python để nhập vào 3 số nguyên từ bàn phím (n là số nguyên 
dương), sau đó tìm và in ra số lớn thứ hai trong các số nguyên đó.
'''
x,y,z = map(float,input("Nhập 3 số nguyên x , y , z : ").split())
if x > y and x < z :
    print("Số lớn thứ hai là : ",x)
if x<y and x>z :
    print("Số lớn thứ hai là : ",x)
if y > x and y < z : 
    print("Số lớn thứ hai là : ",y)
if y < x and y > z :
    print("Số lớn thứ hai là : ",y)
if z > x and z < y :
    print("Số lớn nhất là : ",z)
if z < x and z > y :
    print("Số lớn thứ hai là : ",z)
