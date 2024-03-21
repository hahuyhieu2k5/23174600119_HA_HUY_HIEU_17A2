''' Hãy viết chương trình Python để kiểm tra vị trí tương đối giữa một đường
thẳng và một đường tròn trong không gian hai chiều. Hãy nhập các thông số
của đường thẳng (hệ số góc và hệ số tự do) và các thông số của đường tròn (tọa
độ tâm và bán kính). Sau đó, chương trình sẽ xác định vị trí tương đối giữa
đường thẳng và đường tròn (đường thẳng cắt đường tròn, đường thẳng tiếp
xúc đường tròn, đường thẳng nằm ngoài đường tròn hay đường thẳng nằm
trong đường tròn) và in ra kết quả tương ứng'''
###############################################
''' b1:Nhập vào toạ độ tâm I
    b2:nhập vào hệ số của đường thẳng 
    b3:nhập vào bán kinh đường tròng
    b4:tính khoảng cách từ tâm I đến đường tròn và so sánh với R'''
print("-------------------------------------Bài làm----------------------------------------")
import math
i1,i2=map(int,input("Mời nhập vào toạ độ tâm I:").split())
print("I","(",i1,";",i2,")")
a,b,c=map(int,input("Mời nhập vào hệ số đường thẳng :").split())
print("d1:",a,"x +",b,"y +",c,"= 0")
r=int(input("Mời nhập vào toạ độ bán kính đường tròn :"))
print ("R = ",r)
#Tính khoảng cách từ tâm I --> đường thẳng d1
tu=abs(a*i1+b*i2+c)
mau=math.sqrt(a**2+b**2)
d=tu/mau
print("Khoảng cách từ tâm I-->d1 =",round(d,2))
if d == r:
    print("Đường thẳng d1 tiếp xúc với đường tròn")
elif d>r:
    print("Đường thẳng d1 nằm ngoài đường tròn")
else:
    print("Đường thẳng d1 nằm trong đường tròn")