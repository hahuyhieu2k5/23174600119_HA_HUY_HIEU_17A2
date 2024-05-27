#1
def kiem_tra_so_le(n):
    return n % 2 != 0
danh_sach = [4, 9, 2, 5, 19, 27, 28, 12, 20, 77]
so_le = list(filter(kiem_tra_so_le, danh_sach))
print("Các số lẻ trong danh sách là:", so_le)

#2
def kiem_tra_so_chan(n):
    return n % 2 == 0

def filter_even_numbers(numbers):
    return list(filter(kiem_tra_so_chan, numbers))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print("Các số chẵn trong danh sách:", even_numbers)

#3
def lap_phuong(n):
    return n ** 3
danh_sach_ban_dau = [1, 9, 2, 7]
danh_sach_lap_phuong = list(map(lap_phuong, danh_sach_ban_dau))
print("Danh sách các lập phương của các phần tử trong danh sách ban đầu là:", danh_sach_lap_phuong)

#4
def tinh_lap_phuong(n):
    return n ** 3
def kiem_tra_so_chan(n):
    return n % 2 == 0
def tao_danh_sach_lap_phuong_cua_so_chan(danh_sach):
    return list(map(tinh_lap_phuong, filter(kiem_tra_so_chan, danh_sach)))
danh_sach_ban_dau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
danh_sach_lap_phuong_cua_so_chan = tao_danh_sach_lap_phuong_cua_so_chan(danh_sach_ban_dau)
print("Danh sách các lập phương của các số chẵn trong danh sách ban đầu:", danh_sach_lap_phuong_cua_so_chan)
#5
def tinh_binh_phuong(n):
    return n ** 2
def kiem_tra_so_le(n):
    return n % 2 != 0
def tao_danh_sach_binh_phuong_cua_so_le(danh_sach):
    return list(map(tinh_binh_phuong, filter(kiem_tra_so_le, danh_sach)))
danh_sach_ban_dau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
danh_sach_binh_phuong_cua_so_le = tao_danh_sach_binh_phuong_cua_so_le(danh_sach_ban_dau)
print("Danh sách các bình phương của các số lẻ trong danh sách ban đầu:", danh_sach_binh_phuong_cua_so_le)

