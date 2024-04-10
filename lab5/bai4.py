def is_prime(n):
  """
  Hàm kiểm tra số nguyên tố.

  Tham số:
    n: Số nguyên dương cần kiểm tra.

  Trả về:
    True nếu n là số nguyên tố, False nếu không.
  """
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def main():
  # Nhập chuỗi ký tự từ người dùng
  chuoi = input("Nhập chuỗi ký tự: ")

  # Loại bỏ các ký tự không phải là số
  so_nguyen = ""
  for char in chuoi:
    if char.isdigit():
      so_nguyen += char

  # Kiểm tra xem chuỗi kết quả có phải là số nguyên tố hay không
  if so_nguyen == "":
    print("Chuỗi không chứa số nào.")
  else:
    so_nguyen = int(so_nguyen)
    if is_prime(so_nguyen):
      print(f"{so_nguyen} là số nguyên tố.")
    else:
      print(f"{so_nguyen} không phải là số nguyên tố.")

if __name__ == "__main__":
  main()
