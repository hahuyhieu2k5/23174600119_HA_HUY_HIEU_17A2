import math

class TamGiac:
    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b
        self.c = c if c is not None else math.sqrt(a**2 + b**2)

    def tinh_chu_vi(self):
        return self.a + self.b + self.c

    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

# Kiểm tra
def main():
    tg = TamGiac(3, 4)  # Tam giác vuông
    print(f"Tam giác - Chu vi: {tg.tinh_chu_vi()}, Diện tích: {tg.tinh_dien_tich():.2f}")

    tgc = TamGiac(3, 4, 4)  # Tam giác cân
    print(f"Tam giác cân - Chu vi: {tgc.tinh_chu_vi()}, Diện tích: {tgc.tinh_dien_tich():.2f}")

    tgd = TamGiac(4, 4, 4)  # Tam giác đều
    print(f"Tam giác đều - Chu vi: {tgd.tinh_chu_vi()}, Diện tích: {tgd.tinh_dien_tich():.2f}")

if __name__ == "__main__":
    main()
