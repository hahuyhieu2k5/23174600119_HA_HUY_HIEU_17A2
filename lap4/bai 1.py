def main():
  """
  Hàm chính của chương trình.
  """
  # Biến để lưu trữ tổng các số đã nhập
  tong = 0
  # Biến để đếm số lượng số nguyên đã nhập
  dem = 0
  # Danh sách để lưu trữ các số lẻ đã nhập
  so_le = []
  # Danh sách để lưu trữ các số chẵn đã nhập
  so_chan = []

  # Nhập số nguyên dương từ bàn phím
  while True:
    so = int(input("Nhập số nguyên dương (nhập 0 để kết thúc): "))
    if so == 0:
      break

    # Tăng số lượng số nguyên đã nhập
    dem += 1

    # Cập nhật tổng các số đã nhập
    tong += so

    # Kiểm tra số lẻ hay chẵn
    if so % 2 == 1:
      so_le.append(so)
    else:
      so_chan.append(so)

    # Kiểm tra nếu tổng vượt quá 1000
    if tong > 1000:
      break

  # In ra các số lẻ đã nhập
  print("Các số lẻ đã nhập:")
  for so in so_le:
    print(so, end=" ")
  print()

  # In ra các số chẵn đã nhập
  print("Các số chẵn đã nhập:")
  for so in so_chan:
    print(so, end=" ")
  print()

  # In ra số lượng số nguyên đã nhập
  print("Số lượng các số nguyên đã nhập:", dem)


if __name__ == "__main__":
  main()