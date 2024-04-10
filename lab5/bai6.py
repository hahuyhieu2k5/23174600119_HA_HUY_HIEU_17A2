def dem_ky_tu_dac_biet(chuoi):
  """
  Hàm đếm số lần xuất hiện và tỷ lệ phần trăm của ký tự đặc biệt trong chuỗi.

  Tham số:
    chuoi: Chuỗi ký tự cần kiểm tra.

  Trả về:
    Từ điển chứa số lần xuất hiện và tỷ lệ phần trăm của mỗi ký tự đặc biệt trong chuỗi.
  """
  ky_tu_dac_biet = {}
  for char in chuoi:
    if not char.isalnum():
      if char not in ky_tu_dac_biet:
        ky_tu_dac_biet[char] = 0
      ky_tu_dac_biet[char] += 1
  
  # Tính tỷ lệ phần trăm
  for char in ky_tu_dac_biet:
    ky_tu_dac_biet[char] = round(ky_tu_dac_biet[char] / len(chuoi) * 100, 2)
  return ky_tu_dac_biet

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ")

# Đếm số lần xuất hiện và tỷ lệ phần trăm của ký tự đặc biệt
ky_tu_dac_biet = dem_ky_tu_dac_biet(chuoi)

# In ra kết quả
if ky_tu_dac_biet:
  print("Danh sách các ký tự đặc biệt và tỷ lệ phần trăm xuất hiện:")
  for char, count in ky_tu_dac_biet.items():
    print(f"{char}: {count}%")
else:
  print("Chuỗi không chứa ký tự đặc biệt nào.")
