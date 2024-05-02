'''Tạo một từ điển (tên từ điển là tên của sinh viên), với từ điển là các phần tử mà 
có key là x và value của key là x3
. Hãy viết chương trình nhập vào một số
nguyên N và in ra từ điển dạng như trên với độ dài bằng N.'''


N = int(input("Nhập số nguyên N: "))
if N <= 0:
    print("N phải lớn hơn 0.")
else:
    tran_van_hoa = {}
    for i in range(1, N + 1):
        tran_van_hoa[i] = i ** 3

    print("Từ điển:")
    for key, value in tran_van_hoa.items():
        print(f"{key}: {value}")
