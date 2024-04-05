'''Bài 2:
a) Viết chương trình in ra các số nguyên tố nhỏ hơn 100 (sử dụng vòng lặp 
while)
b) Viết chương trình in ra các số chính phương nhỏ hơn 100 (sử dụng vòng lặp 
while)
c) Viết chương trình để in ra tất cả các số Fibonacci nhỏ hơn 1000 (sử dụng vòng 
lặp while)'''

# In ra các số nguyên tố nhỏ hơn 100 sử dụng vòng lặp while
print("Các số nguyên tố nhỏ hơn 100 là : ")
i = 2
while i < 100:
    check = True
    j = 2
    while j <= i ** 0.5 :
        if i % j == 0:
            check = False
            break
        j += 1
    if check :
        print(i, end=" ")
    i += 1

#In ra các số chính phương nhỏ hơn 100 (sử dụng vòng lặp while)
print("Các số chính phương nhỏ hơn 100 là : ")
i = 0
while i * i < 100:
  print(i * i)
  i += 1

#In ra tất cả các số Fibonacci nhỏ hơn 1000 (sử dụng vòng lặp while)
print("Tất cả các số Fibonacci nhỏ hơn 1000 là :")
i = 0
a , b = 0 , 1
while i < 1000:
    if b >= 1000:
        break
    print(b,end = " ")
    a,b = b , a + b



