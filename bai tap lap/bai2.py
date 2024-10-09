class TS:
    def __init__(self, ho_ten, toan, anh, van):
        self.ho_ten = ho_ten
        self.toan = toan
        self.anh = anh
        self.van = van

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.toan = float(input("Nhập điểm Toán: "))
        self.anh = float(input("Nhập điểm Anh: "))
        self.van = float(input("Nhập điểm Văn: "))

    def tinh_tong_diem(self):
        return self.toan + self.anh + self.van

    def in_thong_tin(self):
        print("Họ tên: {}".format(self.ho_ten))
        print("Tổng điểm: {:.2f}".format(self.tinh_tong_diem()))

n = int(input("Nhập số lượng thí sinh: "))

danh_sach_thi_sinh = []
for i in range(n):
    ts = TS("", 0, 0, 0)
    ts.nhap_thong_tin()
    danh_sach_thi_sinh.append(ts)

# Sắp xếp danh sách theo tổng điểm giảm dần
danh_sach_thi_sinh.sort(key=lambda x: x.tinh_tong_diem(), reverse=True)

diem_chuan = 20

print("Danh sách thí sinh trúng tuyển:")
for ts in danh_sach_thi_sinh:
    if ts.tinh_tong_diem() >= diem_chuan:
        print("Họ tên: {}, Tổng điểm: {:.2f}".format(ts.ho_ten, ts.tinh_tong_diem()))