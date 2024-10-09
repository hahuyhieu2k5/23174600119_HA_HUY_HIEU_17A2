import math

class Hinh:
    def __init__(self, x, y, a, b=None):
        self.x = x
        self.y = y
        self.a = a  # Bán trục lớn hoặc bán kính
        self.b = b if b is not None else a  # Bán trục nhỏ, mặc định bằng bán kính

    def tinh_dien_tich(self):
        return math.pi * self.a * self.b

# Kiểm tra
elip = Hinh(1, 1, 6, 3)
print(f"Diện tích elip: {elip.tinh_dien_tich():.2f}")

duong_tron = Hinh(1, 1, 6)
print(f"Diện tích đường tròn: {duong_tron.tinh_dien_tich():.2f}")
