a=float(input("Hãy nhập độ dài cạnh đáy : "))
h=float(input("Hãy nhập chiều cao : "))
sxq=2*a*h
print("Diện tích xung quanh của hình chóp tứ giác đều là : ".format(sxq))
stp=sxq+a*2
print("Diện tích toàn phần của hình chóp tứ giác đều là : ".format(stp))
scd=a*2
v=1/3*scd*h
print(f"Thể tích của hình chóp tứ giác đều là :{v:.2f}".format(scd,v))



