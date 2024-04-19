'''Viết một chương trình Python để thực hiện các thao tác sau:
+ Cho phép người dùng nhập vào một dãy các số từ bàn phím. Dãy số có thể
bao gồm bất kỳ số nào, có thể là số nguyên, số thực hoặc cả hai.
+ Tìm và in ra màn hình số lớn nhất và số nhỏ nhất trong dãy số đó.'''


day_so = []

while True:
    try:
        user_input = input("Nhập số (nhập 'dừng' để kết thúc): ")
        if user_input.lower() == 'dừng':
            break
        number = float(user_input)
        day_so.append(number)
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

if not day_so:
    print("Dãy số trống.")
else:
    min_number = min(day_so)
    max_number = max(day_so)

    print("Số nhỏ nhất:", min_number)
    print("Số lớn nhất:", max_number)

