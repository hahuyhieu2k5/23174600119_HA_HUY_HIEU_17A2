def tim_kiem_tu(chuoi, tu_can_tim):
  """
  Hàm tìm kiếm và đếm số lần xuất hiện của từ trong chuỗi.

  Tham số:
    chuoi: Chuỗi văn bản cần tìm kiếm.
    tu_can_tim: Từ cần tìm kiếm.

  Trả về:
    Vị trí (index) của từ cần tìm trong chuỗi và số lần xuất hiện của từ đó.
  """
  vi_tri = -1
  so_lan_xuat_hien = 0
  for i in range(len(chuoi)):
    if chuoi[i:].startswith(tu_can_tim):
      vi_tri = i
      so_lan_xuat_hien += 1
  return vi_tri, so_lan_xuat_hien

def dem_so_lan_xuat_hien(chuoi, tu_can_tim):
  """
  Hàm đếm số lần xuất hiện của từ trong chuỗi.

  Tham số:
    chuoi: Chuỗi văn bản cần tìm kiếm.
    tu_can_tim: Từ cần tìm kiếm.

  Trả về:
    Số lần xuất hiện của từ trong chuỗi.
  """
  so_lan_xuat_hien = 0
  for i in range(len(chuoi)):
    if chuoi[i:].startswith(tu_can_tim):
      so_lan_xuat_hien += 1
  return so_lan_xuat_hien

def tim_tu_xuat_hien_nhieu_nhat(chuoi):
  """
  Hàm tìm từ xuất hiện nhiều nhất trong chuỗi.

  Tham số:
    chuoi: Chuỗi văn bản cần tìm kiếm.

  Trả về:
    Từ xuất hiện nhiều nhất trong chuỗi và số lần xuất hiện của từ đó.
  """
  tu_xuat_hien_nhieu_nhat = ""
  so_lan_xuat_hien_nhieu_nhat = 0
  for tu in chuoi.split():
    so_lan_xuat_hien = dem_so_lan_xuat_hien(chuoi, tu)
    if so_lan_xuat_hien > so_lan_xuat_hien_nhieu_nhat:
      tu_xuat_hien_nhieu_nhat = tu
      so_lan_xuat_hien_nhieu_nhat = so_lan_xuat_hien
  return tu_xuat_hien_nhieu_nhat, so_lan_xuat_hien_nhieu_nhat

# Nhập chuỗi văn bản từ người dùng
chuoi = input("Nhập chuỗi văn bản: ")

# Nhập từ cần tìm kiếm
tu_can_tim = input("Nhập từ cần tìm kiếm: ")

# Tìm kiếm và đếm số lần xuất hiện của từ
vi_tri, so_lan_xuat_hien = tim_kiem_tu(chuoi, tu_can_tim)

# In ra kết quả
print(f"Từ '{tu_can_tim}' xuất hiện lần đầu tiên tại vị trí {vi_tri} và xuất hiện {so_lan_xuat_hien} lần trong chuỗi.")

# Tìm từ xuất hiện nhiều nhất
tu_xuat_hien_nhieu_nhat, so_lan_xuat_hien_nhieu_nhat = tim_tu_xuat_hien_nhieu_nhat(chuoi)

# In ra kết quả
print(f"Từ xuất hiện nhiều nhất trong chuỗi là '{tu_xuat_hien_nhieu_nhat}' với {so_lan_xuat_hien_nhieu_nhat} lần xuất hiện.")
