'''Viết một chương trình Python để thực hiện các yêu cầu sau:
a) Dãy Fibonacci:
Tạo một danh sách chứa n số Fibonacci đầu tiên, trong đó n được người dùng 
nhập từ bàn phím.
Yêu cầu: Sử dụng list comprehension để tạo danh sách này.
b) Danh sách số nguyên tố:
Tạo một danh sách chứa tất cả các số nguyên tố nhỏ hơn 100'''
a, b = 0 , 1
Fibonacci = []
import random
n = int(input("Số phần tử: "))
danh_sach_A = [int(input("Nhập vào phần tử trong danh sách: ")) for _ in range(n)]
for i in range(0,1000): 
    print(n, end=" ")
    a, b = b, a + b




