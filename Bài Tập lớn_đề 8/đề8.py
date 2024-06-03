import random
import csv
#1
def tao_danh_sach_nguoi_tham_gia():
    return ["Hiếu", "Khánh", "Thắng", "Thái", "Chuyên", "Thành", "Qúy", "Hùng", "Dũng","Ngọc Anh", "Đạt", "Khôi", "Hưng", "Hòa", "Tâm"]

def tao_set_nguoi_da_chia():
    return set()

def tao_dict_so_luong_nguoi_trong_nhom():
    return {}

def chia_nhom(nguoi_tham_gia):
    so_nguoi = len(nguoi_tham_gia)
    so_nhom = so_nguoi // 3
    
    random.shuffle(nguoi_tham_gia)
    
    nhom = {}
    for i in range(so_nhom):
        nhom[f'Nhóm {i+1}'] = nguoi_tham_gia[i*3:(i+1)*3]
        
    for i in range(so_nhom*3, so_nguoi):
        nhom[f'Nhóm {i % so_nhom + 1}'].append(nguoi_tham_gia[i])
    
    return nhom

def xac_suat_chia_nhom(nguoi_tham_gia, ten_nguoi, nhom):
    so_lan_xuat_hien = sum([1 for thanh_vien in nhom.values() if ten_nguoi in thanh_vien])
    return so_lan_xuat_hien / len(nhom)

def hien_thi_danh_sach_nhom(nhom):
    for ten_nhom, thanh_vien in nhom.items():
        print(f"{ten_nhom}: {', '.join(thanh_vien)}")

def luu_ket_qua_csv(nhom):
    with open('ket_qua.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Tên nhóm', 'Thành viên']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for ten_nhom, thanh_vien in nhom.items():
            writer.writerow({'Tên nhóm': ten_nhom, 'Thành viên': ', '.join(thanh_vien)})

if __name__ == "__main__":
    nguoi_tham_gia = tao_danh_sach_nguoi_tham_gia()
    
    nhom = chia_nhom(nguoi_tham_gia)
    hien_thi_danh_sach_nhom(nhom)
    
    luu_ket_qua_csv(nhom)  

 

