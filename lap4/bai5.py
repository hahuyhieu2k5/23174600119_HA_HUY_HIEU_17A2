import math
while True:
    # Nhập hai số từ người dùng
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    print("Kết quả các phép tính:")
    print("Tổng:", a + b)
    print("Hiệu:", a - b)
    print("Tích:", a * b)
    if b != 0:
        print("Thương:", a / b)
    else:
        print("Không thể chia cho 0")

    print("Lũy thừa:", a ** b)
    if b >= 0:
        print("Căn bậc hai của số thứ nhất:", math.sqrt(a))
        print("Căn bậc hai của số thứ hai:", math.sqrt(b))
    else:
        print("Không thể tính căn bậc hai của số âm")
    choice = input("Bạn có muốn tiếp tục không? (yes/no): ")
    if choice.lower() != 'yes':
        break
print("Kết thúc chương trình.")