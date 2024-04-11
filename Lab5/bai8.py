'''
Viết một chương trình Python để thực hiện các yêu cầu sau trên một chuỗi ký 
tự có độ dài hơn 10 ký tự.
a) Trích ra chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8.
b) Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5.
c) Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự.
d) Chuyển đổi các ký tự trong chuỗi thành chữ thường.
e) Chuyển đổi các ký tự trong chuỗi thành chữ hoa.
f) Đảo ngược chuỗi ký tự vừa nhập.
'''

n = input("Hãy nhập chuỗi gồm 10 ký tự :")
print("a) Trích ra chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8 là : ")
print(n[1:8])

print("b) Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5 là : ")
print(n[4:])

print("c) Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự là : ")
print(n[:6:-1])

print("d) Chuyển đổi các ký tự trong chuỗi thành chữ thường là : ")
print(n.lower())

print("e) Chuyển đổi các ký tự trong chuỗi thành chữ hoa là : ")
print(n.upper())

print("f) Đảo ngược chuỗi ký tự vừa nhập là : ")
print(n[::-1])
