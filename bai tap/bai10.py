print('--------------------------------Bài làm-----------------------------')
loai_phim=input("Mời quý khách chọn thể loại phim :")
gio_xem=input("Mời quý khách chọn thời gian muốn xem phim:")
if loai_phim=="Hành động" or loai_phim=="Kinh dị" or loai_phim=="Tình cảm"or loai_phim=="Hài hước"or loai_phim=="Hoạt hình":
    if loai_phim=="Hành động" and( gio_xem =="Sáng" or gio_xem=="Chiều" or gio_xem=="Tối"):
        print("""Sáng:8h-12h
                     Chiều:13h-16h
                     Tối:17h-23h""")
    elif loai_phim=="Kinh dị" and gio_xem=="Tối":
        print("Tối :19h-23h")
    elif loai_phim=="Tình cảm" and gio_xem=="Tối":
        print("Tối :19h-23h")
    elif loai_phim=="Hài hước" and( gio_xem =="Sáng" or gio_xem=="Chiều" or gio_xem=="Tối"):
        print("""Sáng:8h-12h
                     Chiều:13h-16h
                     Tối:17h-23h""")
    elif loai_phim=="Hoạt hình" and (gio_xem=="Sáng" or gio_xem=="Chiều"):
        print(""" Sáng 8h-12h
                  Chiều 13h-17h""")
    else:
        print("Không có suất chiếu")
        

