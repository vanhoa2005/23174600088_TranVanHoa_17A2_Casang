# Bài 1
'''Viết chương trình nhập vào các hệ số a, b và in ra nghiệm của phương trình bậc 
nhất: ax + b = 0 (giải và biện luận đầy đủ các trường hợp).'''
a,b = map(float,input("Nhập các hệ số a,b : ").split())
if a !=0 :  
    x = -b /a
    print("Phương trình có nghiệm là :",x)
if a ==0:
     print("Phương trình vô nghiệm !")

    