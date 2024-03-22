'''Hãy viết chương trình Python để xác định vị trí tương đối của hai đường thẳng 
trong không gian hai chiều. Hãy nhập thông số của hai đường thẳng (hệ số góc 
và hệ số tự do) và in ra kết quả vị trí tương đối của hai đường thẳng (đường 
thẳng song song, đường thẳng cắt nhau hay đường thẳng vuông góc).
'''


a1 , b1  = map(float,input("Nhập hệ số của đường thẳng thứ nhất :").split())
a2 , b2  = map(float,input("Nhập hệ số của đường thẳng thứ hai :").split())
if a1 == a2 and b1 != b2 :
    print("Hai đường thẳng song song với nhau")
if a1 != a2 :
    print("Hai đường thẳng cắt nhau")
if a1 * a2 == -1 :
    print("Hai đường thẳng vuông góc với nhau")

