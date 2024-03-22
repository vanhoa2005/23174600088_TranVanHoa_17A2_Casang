'''Viết chương trình Python để tính tổng số tiền phải trả khi mua vé xem phim 
với số lượng người khác nhau, trong đó:
+ Giá vé cho 1 người là 120.000 đồng.
+ Nếu số người là 2 đến 4, giảm 5% tổng số tiền.
+ Nếu số người là 4 đến 10, giảm 10% tổng số tiền.
+ Nếu số người là từ 10 người trở lên, giảm 20% tổng số tiền.
Số lượng người sẽ được nhập từ bàn phím.
'''
luong_nguoi = int(input("Nhập lượng người cùng mua vé xem phim : "))
gia_ve_1_nguoi = 1200000
tong = gia_ve_1_nguoi * luong_nguoi
if luong_nguoi == 1 :
    print("Tổng số tiền phải trả khi mua vé xem phim là :",tong,"đồng")
elif 2 <= luong_nguoi < 4 :
    giam1= 0.05
    print("Tổng số tiền phải trả khi mua vé xem phim là : ",tong -tong * giam1,"đồng")    
elif 4 <= luong_nguoi < 10 :
    giam2 = 0.1
    print("Tổng số tiền phải trả khi mua vé xem phim là : ",tong -tong * giam2,"đồng")  
elif luong_nguoi >= 10 :
    giam3= 0.2
    print("Tổng số tiền phải trả khi mua vé xem phim là : ",tong -tong * giam3,"đồng")          