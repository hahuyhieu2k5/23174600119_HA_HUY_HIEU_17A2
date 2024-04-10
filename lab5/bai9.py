def co_the_bien_doi(chuoi_1, chuoi_2):
  """
  Hàm kiểm tra xem có thể biến đổi chuỗi 1 thành chuỗi 2 bằng cách thêm, xóa hoặc thay đổi một số ký tự hay không.

  Tham số:
    chuoi_1: Chuỗi ký tự ban đầu.
    chuoi_2: Chuỗi ký tự mục tiêu.

  Trả về:
    True nếu có thể biến đổi, False nếu không.
  """
  # Đếm số lượng ký tự khác nhau
  so_luong_khac_biet = 0
  for char_1, char_2 in zip(chuoi_1, chuoi_2):
    if char_1 != char_2:
      so_luong_khac_biet += 1

  # Kiểm tra điều kiện biến đổi
  return so_luong_khac_biet <= 1

# Nhập hai chuỗi từ người dùng
chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")

# Kiểm tra khả năng biến đổi
if co_the_bien_doi(chuoi_1, chuoi_2):
  print("Có thể biến đổi chuỗi thứ nhất thành chuỗi thứ hai.")
else:
  print("Không thể biến đổi chuỗi thứ nhất thành chuỗi thứ hai.")
