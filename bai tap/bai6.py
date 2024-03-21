''' Viết chương trình Python để nhập vào 3 số nguyên từ bàn phím (n là số nguyên
dương), sau đó tìm và in ra số lớn thứ hai trong các số nguyên đó.'''
##########################################
a,b,c=map(int,input("Mời nhập vào 3 số nguyên dương :").split())
if a >= b >= c or c >= b >= a:
    print(b,"Là số lớn thứ 2")
elif b >= a >= c or c >= a >= b:
    print(a,"Là số lớn thứ 2 ")
else:
    print(c,"Là số lớn thứ 2")