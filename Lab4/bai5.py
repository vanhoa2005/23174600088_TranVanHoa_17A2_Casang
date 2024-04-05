'''Bài 5:
Viết chương trình thực hiện các phép tính số học trên hai số nhập từ người 
dùng và cho phép người dùng tiếp tục nếu muốn (sử dụng vòng lặp while).
Yêu cầu:
+ Chương trình yêu cầu người dùng nhập hai số từ bàn phím.
+ Chương trình thực hiện các phép tính cộng, trừ, nhân, chia, lũy thừa và tính 
căn bậc hai của hai số này.
+ Sau mỗi phép tính, chương trình hỏi người dùng có muốn tiếp tục không và 
chờ đợi phản hồi của người dùng để quyết định tiếp tục hay kết thúc chương 
trình.'''


a, b = map(int, input("Nhập vào hai số a và b: ").split())
print("""Chương trình hiển thị menu chọn phép toán:
1. Phép cộng 2 số
2. Phép trừ 2 số
3. Phép nhân 2 số
4. Phép chia 2 số
5. Lũy thừa 2 số
6. Căn bậc hai của 2 số
0. Thoát chương trình""")
lua_chon = int(input("Nhập vào lựa chọn: "))
while True:
    if lua_chon == 1:
        print(f"Tổng 2 số là: {a} + {b} = {a + b}")
        break
    elif lua_chon == 2:
        print(f"Hiệu 2 số là: {a} - {b} = {a - b}")
        break
    elif lua_chon == 3:
        print(f"Tích 2 số là: {a} x {b} = {a * b}")
        break
    elif lua_chon == 4:
        print(f"Thương 2 số là: {a} : {b} = {a / b}")
        break
    elif lua_chon == 5 :
        print(f"Lũy thừa của {a} với {b} = {a**b} và {b} với {a} = {b**a}")
        break
    elif lua_chon == 6 :
        print(f"Căn bậc hai của {a} = {a**0.5} và {b} = {b**0.5}")
        break
    elif lua_chon == 0:
        break
    else:
        print("Lựa chọn sai, vui lòng nhập lại")



