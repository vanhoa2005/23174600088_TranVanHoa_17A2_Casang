'''
Viết chương trình Python nhận vào điểm số của một bài kiểm tra từ người dùng 
và in ra một thông báo tương ứng theo quy tắc sau:
+ Nếu điểm số từ 0 đến 5, in ra "Điểm kém"
+ Nếu điểm số từ 5 đến 7, in ra "Điểm trung bình"
+ Nếu điểm số từ 7 đến 8.5, in ra "Điểm khá"
+ Nếu điểm số từ 8.5 đến 10, in ra "Điểm tốt"
'''
n = float(input("Nhập điểm số của bài kiểm tra : "))
if 0 <= n < 5 :
    print("Điểm kém !")
elif 5 <= n < 7 :
    print("Điểm trung bình !")
elif 7 <= n < 8.5 :
    print("Điểm khá !") 
elif 8.5 <= n <= 10 :
    print("Điểm giỏi !")

