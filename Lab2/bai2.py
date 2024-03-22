'''Viết chương trình Python nhận vào một số nguyên từ người dùng và xuất ra 
chữ số hàng nghìn của số đó, nếu không có thì xuất ra 0.'''
n = int(input("Nhập vào một số nguyên :"))
if 100 <= n <= 9999 :
    chu_so_hang_nghin = n // 1000
    print("Chữ số hàng nghìn có chữ số {} là : {} ".format(n,chu_so_hang_nghin))
