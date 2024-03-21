''' Viết chương trình Python nhận vào một số nguyên từ người dùng và xuất ra
chữ số hàng nghìn của số đó, nếu không có thì xuất ra 0.'''
a=int(input("Mời nhập vào chữ số nguyên bất kỳ :"))
if a>1000:
    chu_so=a//1000
    print("Chữ số hàng nghìn bạn vừa nhập là :",chu_so)
else:
    print("Chữ số hàng nghìn bạn vừa nhập là :0")