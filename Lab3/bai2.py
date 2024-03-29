''' Viết chương trình để tính tổng các số chia hết cho 7 nhưng không chia hết 
cho 5 trong khoảng từ 2000 đến 4000.'''
print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng từ 2000 đến 4000 là : ")
for i in range(2000,4001,1):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end = " ")

''' Viết chương trình để tính tổng các số chia hết cho 4 nhưng không chia hết 
cho 6 trong khoảng từ 500 đến 1000'''
print("Tổng các số chia hết cho 4 nhưng không chia hết cho 6 trong khoảng từ 500 đến 1000 là :")
for i in range(500,1001,1):
    if i % 4 == 0 and i % 6 != 0 :
        print(i,end = " ")

