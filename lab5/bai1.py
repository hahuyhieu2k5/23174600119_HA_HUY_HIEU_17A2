def chuyen_doi_nhi_phan(so_thap_phan):
  """
  Hàm chuyển đổi số thập phân sang số nhị phân.

  Tham số:
    so_thap_phan: Số nguyên dương (số thập phân)

  Trả về:
    Chuỗi biểu diễn số nhị phân của số thập phân được nhập.
  """
  so_nhi_phan = ""
  while so_thap_phan > 0:
    so_du = so_thap_phan % 2
    so_thap_phan //= 2
    so_nhi_phan = str(so_du) + so_nhi_phan
  return so_nhi_phan

# Nhập số thập phân từ người dùng
so_thap_phan = int(input("Nhập số thập phân: "))

# Chuyển đổi số thập phân sang số nhị phân
so_nhi_phan = chuyen_doi_nhi_phan(so_thap_phan)

# In ra kết quả
print(f"Số nhị phân của {so_thap_phan} là: {so_nhi_phan}")