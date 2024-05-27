# Tạo từ điển kho và từ điển giá tiền
kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
mua_hang = {
    "banana": 2,
    "apple": 3,
    "orange": 1,
    "pear": 4
}
hoa_don = {}  
tong_tien = 0  

for mat_hang, so_luong in kho.items():
    if mat_hang in gia_tien:
        don_gia = gia_tien[mat_hang]  
        thanh_tien = so_luong * don_gia 
        hoa_don[mat_hang] = {"So luong": so_luong, "Don gia": don_gia, "Thanh tien": thanh_tien}
        tong_tien += thanh_tien  
print("Hóa đơn mua hàng:")
for mat_hang, thong_tin in hoa_don.items():
    print(f"Mặt hàng: {mat_hang}, Số lượng: {thong_tin['So luong']}, Đơn giá: {thong_tin['Don gia']}, Thành tiền: {thong_tin['Thanh tien']}")
print(f"Tổng tiền: {tong_tien}")
print("\nSố lượng của các mặt hàng trong kho sau khi mua hàng:")
for mat_hang, so_luong in kho.items():
    print(f"{mat_hang}: {so_luong}")