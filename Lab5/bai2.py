'''Viết một chương trình Python nhận đầu vào là hai chuỗi ký tự str1 và str2, sau 
đó tìm ra chuỗi ký tự con chung có độ dài ngắn nhất của hai chuỗi này.'''

chuoi1 = input("Nhập chuỗi thứ nhất: ")
chuoi2 = input("Nhập chuỗi thứ hai: ")
chuoi = [[0 for _ in range(len(chuoi2) + 1)] for _ in range(len(chuoi1) + 1)]
for i in range(len(chuoi1) + 1):
    for j in range(len(chuoi2) + 1):
        if i == 0 or j == 0:
            chuoi[i][j] = 0
        elif chuoi1[i - 1] == chuoi2[j - 1]:
            chuoi[i][j] = chuoi[i - 1][j - 1] + 1
        else:
            chuoi[i][j] = max(chuoi[i - 1][j], chuoi[i][j - 1])

i = len(chuoi1)
j = len(chuoi2)
ngan_nhat = ""
while i > 0 and j > 0:
    if chuoi1[i - 1] == chuoi2[j - 1]:
        ngan_nhat = chuoi1[i - 1] + ngan_nhat
        i -= 1
        j -= 1
    else:
        if chuoi[i - 1][j] > chuoi[i][j - 1]:
            i -= 1
        else:
            j -= 1
print(f"Chuỗi con chung ngắn nhất: {ngan_nhat}")
