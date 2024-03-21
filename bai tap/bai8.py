''' Hãy viết chương trình Python để xác định vị trí tương đối của hai đường thẳng
trong không gian hai chiều. Hãy nhập thông số của hai đường thẳng (hệ số góc
và hệ số tự do) và in ra kết quả vị trí tương đối của hai đường thẳng (đường
thẳng song song, đường thẳng cắt nhau hay đường thẳng vuông góc)'''
######################################################
a1,b1=map(int,input("Mời nhập hệ số vào đường thẳng d1:").split())
a2,b2=map(int,input("Mời nhập hệ số vào đường thẳng d2:").split())
if a1 == a2:
    print( "Hai đường thẳng là đường thẳng song song.")
    # Kiểm tra nếu hai đường thẳng có hệ số góc nhân với nhau bằng -1 (vuông góc)
elif a1 * a2 == -1:
    print("Hai đường thẳng là đường thẳng vuông góc.")
    # Trường hợp còn lại là hai đường thẳng cắt nhau
else:
    print( "Hai đường thẳng cắt nhau.")