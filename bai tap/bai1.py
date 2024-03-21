''' Viết chương trình nhập vào các hệ số a, b và in ra nghiệm của phương trình bậc
nhất: ax + b = 0 (giải và biện luận đầy đủ các trường hợp)'''
a,b=map(int,input("Mời nhập vào 2 giá trị a,b:").split())
print(a,"X +",b,"= 0")
if a==0:
    print("Phương trình bậc nhất vô nghiệm")
elif b==0:
    print("X = 0")
else:
    print("X = ",-b/a)