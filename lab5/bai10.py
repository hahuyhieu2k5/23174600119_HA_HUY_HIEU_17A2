def xoa_khoang_trang(chuoi):
  """
  Hàm xóa tất cả các khoảng trắng giữa các ký tự trong chuỗi.

  Tham số:
    chuoi: Chuỗi ký tự cần xử lý.

  Trả về:
    Chuỗi mới sau khi xóa khoảng trắng.
  """
  return "".join(chuoi.split())

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ")

# Xóa khoảng trắng
chuoi_moi = xoa_khoang_trang(chuoi)

# In ra kết quả
print(f"Chuỗi sau khi xóa khoảng trắng: {chuoi_moi}")


