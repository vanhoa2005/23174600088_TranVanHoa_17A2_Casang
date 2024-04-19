'''Viết một chương trình Python để thực hiện các thao tác sau:
+ Cho phép người dùng nhập vào một dãy các số nguyên từ bàn phím. Dãy số
có thể chứa bất kỳ số nào.
+ Kiểm tra xem dãy số đó có tạo thành cấp số cộng không.
+ Nếu dãy số tạo thành cấp số cộng, xuất ra màn hình dãy số và thông báo rằng 
dãy số này tạo thành cấp số cộng. Nếu không, xuất ra thông báo tương ứng'''

n = int(input("Nhập số lượng phần tử: "))
day_so = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i + 1}: "))
    day_so.append(so)

co_phai_cap_so_cong = True

for i in range(1, n):
    if day_so[i] - day_so[i - 1] != day_so[1] - day_so[0]:
        co_phai_cap_so_cong = False

if co_phai_cap_so_cong:
    print(f"Dãy số {day_so} là cấp số cộng.")
else:
    print(f"Dãy số {day_so} không phải là cấp số cộng.")











