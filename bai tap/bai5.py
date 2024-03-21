''' Viết chương trình Python để tính tổng số tiền phải trả khi mua vé xem phim
với số lượng người khác nhau, trong đó :
+ Giá vé cho 1 người là 120.000 đồng.
+ Nếu số người là 2 đến 4, giảm 5% tổng số tiền
 Nếu số người là 4 đến 10, giảm 10% tổng số tiền.
+ Nếu số người là từ 10 người trở lên, giảm 20% tổng số tiền.
Số lượng người sẽ được nhập từ bàn phím.'''
#######################################
gia_ve = 120000  # Giá vé cho một người
n=int(input("Mời nhập số vé muốn mua:"))
tong_tien = n * gia_ve
if 2 <= n <= 4:
        tong_tien *= 0.95  
elif 4 < n <= 10:
        tong_tien *= 0.9  
elif n > 10:
        tong_tien *= 0.8  
print("Số tiền quý khách phải trả cho cuộc chơi là :",tong_tien)