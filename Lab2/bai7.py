'''Viết chương trình Python để tính chỉ số BMI (Body Mass Index) dựa trên chiều 
cao và cân nặng được nhập từ người dùng. Chỉ số BMI được tính bằng cách 
chia cân nặng (kg) cho bình phương chiều cao (mét). Sau đó, in kết quả chỉ số
BMI và phân loại BMI ra màn hình.
Chương trình sẽ phân loại chỉ số BMI như sau:
+ Nếu chỉ số BMI nhỏ hơn 18.5, sẽ hiển thị phân loại "Gầy".
+ Nếu chỉ số BMI từ 18.5 đến 24.9, sẽ hiển thị phân loại "Bình thường".
+ Nếu chỉ số BMI từ 25.0 đến 29.9, sẽ hiển thị phân loại "Hơi béo".
+ Nếu chỉ số BMI lớn hơn hoặc bằng 30.0, sẽ hiển thị phân loại "Béo"
'''

chieu_cao = float(input("Hãy nhập chiều cao(mét) : "))
can_nang = float(input("Hãy nhập cân nặng(kg) : "))
BMI = can_nang / chieu_cao **2
if BMI < 18.5 :
    print("Gầy")
if 18.5 < BMI < 24.9 :
    print("Bình thường")
if 25.0 < BMI < 29.9 :
    print("Hơi béo")
if BMI >= 30.0 :
    print("Béo")