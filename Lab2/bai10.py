'''Viết một chương trình Python cho người dùng có thể lựa chọn các thể loại phim 
như Hành động, Kinh dị, Tình cảm, Hài hước và Hoạt hình. Sau đó, yêu cầu 
người dùng nhập lựa chọn thể loại phim và thời gian muốn xem phim (sáng, 
trưa, chiều, tối). Cuối cùng, chương trình sẽ hiển thị thông báo về thời gian 
chiếu phim tương ứng với lựa chọn của người dùng. Hãy lưu ý rằng phim Tình 
cảm chỉ được chiếu vào buổi tối, phim hoạt hình chỉ được chiếu vào buổi sáng 
và trưa, phim kinh dị chỉ được chiếu vào buổi tối. Nếu thời gian chọn không có 
suất chiếu, hãy in ra thông báo "Không có suất chiếu”.
'''


print('''Những thể loại phim bạn muốn xem : hành động , kinh dị , tình cảm , hài hước , hoạt hình ''')
print('''Khoảng thời gian phim chiếu : sáng , trưa , chiều , tối ''')
the_loai_phim = input("Nhập thể loại phim bạn muốn xem : ")
thoi_gian = input("Nhập thời gian bạn muốn xem : ")
if the_loai_phim == "tình cảm":
    if thoi_gian == "tối" :
      print("Phim được chiếu vào lúc 8h")
    else :
       print("Không có suất chiếu")
if the_loai_phim == "hoạt hình" :
    if thoi_gian == "sáng" :
      print("Chương trình được chiếu vào lúc 6h sáng")
    elif thoi_gian == "trưa":
       print("Chương trình được chiếu vào lúc 12h trưa")
    else :
       print("Không có suất chiếu")
if the_loai_phim == "kinh dị" :
    if thoi_gian == "tối":
      print("Chương trình được chiếu vào lúc 10h tối")
    else :
      print("không có suất chiếu")
if the_loai_phim == "hành động":
    if thoi_gian == "sáng":
      print("Chương trình được chiếu vào lúc 8h sáng ")
    elif thoi_gian == "trưa":
      print("Chương trình được chiếu vào lúc 10h trưa")
    elif thoi_gian == "chiều":
       print("Chương trình được chiếu vào lúc 3h chiều")
    elif thoi_gian == "tối":
       print("Chương trình được chiếu vào lúc 7h tối")
     
    
