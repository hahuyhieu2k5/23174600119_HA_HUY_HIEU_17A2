def main():
  """
  Hàm chính của chương trình.
  """
  # Nhập số nguyên n
  n = int(input("Nhập số nguyên n (n > 10): "))
  while n <= 10:
    n = int(input("Nhập số nguyên n (n > 10): "))

  # Biến để lưu trữ tổng
  tong_a = 0
  tong_b = 0
  tong_c = 2
  tong_d = 0

  # Biến để đếm số hạng
  a = 1

  # Vòng lặp while để tính tổng
  while a <= n:
    # Tính tổng cho câu a)
    tong_a += a / 6

    # Tính tổng cho câu b)
    tong_b += 1 / 3

    # Tính tổng cho câu c)
    tong_c += (-1) ** (a - 1) * a / a

    # Tính tổng cho câu d)
    if a > 2:
      tong_d += (a - 1) / (a * (a + 1) * (a + 2))

    # Tăng số hạng
    a += 1

  # In ra kết quả
  print("Câu a) S =", tong_a)
  print("Câu b) S =", tong_b)
  print("Câu c) S =", tong_c)
  print("Câu d) S =", tong_d)


if __name__ == "__main__":
  main()