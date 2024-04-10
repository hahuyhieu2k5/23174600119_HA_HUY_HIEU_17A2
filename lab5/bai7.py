def dem_so_luong_ky_tu(chuoi):
  """
  Hàm đếm số lượng chữ thường, chữ hoa, chữ số và ký tự đặc biệt trong chuỗi.

  Tham số:
    chuoi: Chuỗi ký tự cần kiểm tra.

  Trả về:
    Từ điển chứa số lượng của từng loại ký tự trong chuoi.
  """
  so_luong_ky_tu = {
    "chu_thuong": 0,
    "chu_hoa": 0,
    "chu_so": 0,
    "ky_tu_dac_biet": 0,
  }
  for char in chuoi:
    if char.islower():
      so_luong_ky_tu["chu_thuong"] += 1
    elif char.isupper():
      so_luong_ky_tu["chu_hoa"] += 1
    elif char.isdigit():
      so_luong_ky_tu["chu_so"] += 1
    else:
      so_luong_ky_tu["ky_tu_dac_biet"] += 1
  return so_luong_ky_tu

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ")

# Đếm số lượng của từng loại ký tự
so_luong_ky_tu = dem_so_luong_ky_tu(chuoi)

# In ra kết quả
print("Số lượng các loại ký tự trong chuỗi:")
for loai_ky_tu, so_luong in so_luong_ky_tu.items():
  print(f"{loai_ky_tu}: {so_luong}")
