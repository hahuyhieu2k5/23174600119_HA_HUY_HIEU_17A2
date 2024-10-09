class DaGiac:
    def __init__(self, *canh):
        self.canh = canh

    def tinh_chu_vi(self):
        return sum(self.canh)

class HinhBinhHanh(DaGiac):
    def tinh_dien_tich(self, h):
        return self.canh[0] * h

class HinhChuNhat(HinhBinhHanh):
    def tinh_dien_tich(self):
        return self.canh[0] * self.canh[1]

class HinhVuong(HinhChuNhat):
    def __init__(self, a):
        super().__init__(a, a)

# Kiểm tra
hbh = HinhBinhHanh(7, 3)
print(f"Hình bình hành - Chu vi: {hbh.tinh_chu_vi()}, Diện tích (h=5): {hbh.tinh_dien_tich(5)}")

hcn = HinhChuNhat(5, 6)
print(f"Hình chữ nhật - Chu vi: {hcn.tinh_chu_vi()}, Diện tích: {hcn.tinh_dien_tich()}")

hv = HinhVuong(4)
print(f"Hình vuông - Chu vi: {hv.tinh_chu_vi()}, Diện tích: {hv.tinh_dien_tich()}")
