'''Viết chương trình nhập vào một số nguyên và in ra số chữ số của số nguyên đó
(sử dụng vòng lặp while).
Ví dụ: Số nguyên nhập vào 2946
Số chữ số của số nguyên: 4'''

a = 0
n = int(input("Nhập vào một số nguyên :"))
while n > 0 :
    n //= 10
    a +=1
print("Số chữ số của số nguyên là :",a)


   
