''' Viết chương trình Python nhận vào điểm số của một bài kiểm tra từ người dùng
và in ra một thông báo tương ứng theo quy tắc sau:
+ Nếu điểm số từ 0 đến 5, in ra "Điểm kém"
+ Nếu điểm số từ 5 đến 7, in ra "Điểm trung bình"
+ Nếu điểm số từ 7 đến 8.5, in ra "Điểm khá"
+ Nếu điểm số từ 8.5 đến 10, in ra "Điểm tốt'''
print("-------------------------------Bài làm-----------------------------")
a=float(input("Mời nhập vào số điểm:"))
if a<5:
    print("Điểm kém ")
elif a>=5 and a<7:
    print("Điểm trung bình")
elif a>=7 and a<8.5:
    print("Điểm khá")
elif a>=8.5 and a<=10:
    print("Điểm tốt")