def xep_loai_diem(diem):
    if diem < 4.0:
        return 'F'
    elif 4.0 <= diem < 5.5:
        return 'D'
    elif 5.5 <= diem < 7.0:
        return 'C'
    elif 7.0 <= diem < 8.5:
        return 'B'
    else:
        return 'A'
sinh_vien = {}
for i in range(1, 11):
    ten_sv = input(f"Nhập tên của sinh viên {i}: ")
    diem_thi = float(input(f"Nhập điểm thi của sinh viên {i}: "))
    sinh_vien[ten_sv] = diem_thi

# Thống kê số lượng sinh viên ở mỗi loại học lực
so_luong_loai_hoc_luc = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for ten_sv, diem in sinh_vien.items():
    loai_hoc_luc = xep_loai_diem(diem)
    so_luong_loai_hoc_luc[loai_hoc_luc] += 1
print("Thống kê số lượng sinh viên ở mỗi loại học lực:")
for loai, so_luong in so_luong_loai_hoc_luc.items():
    print(f"Loại {loai}: {so_luong} sinh viên")
