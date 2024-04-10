def trộn_chuỗi(chuỗi1, chuỗi2):
  """
  Hàm trộn hai chuỗi ký tự theo quy tắc:
    + Lần lượt từ trái sang phải, viết các ký tự của chuỗi đầu tiên, sau đó đến chuỗi thứ hai.
    + Thêm một dấu gạch nối '-' giữa các ký tự của hai chuỗi.

  Tham số:
    chuỗi1: Chuỗi ký tự thứ nhất.
    chuỗi2: Chuỗi ký tự thứ hai.

  Trả về:
    Chuỗi kết quả sau khi trộn.
  """
  chuỗi_kết_quả = ""
  for i in range(max(len(chuỗi1), len(chuỗi2))):
    chuỗi_kết_quả += chuỗi1[i] if i < len(chuỗi1) else "-"
    chuỗi_kết_quả += chuỗi2[i] if i < len(chuỗi2) else "-"
  return chuỗi_kết_quả

# Nhập hai chuỗi từ người dùng
chuỗi1 = input("Nhập chuỗi thứ nhất: ")
chuỗi2 = input("Nhập chuỗi thứ hai: ")

# Trộn hai chuỗi
chuỗi_kết_quả = trộn_chuỗi(chuỗi1, chuỗi2)

# In ra kết quả
print(f"Chuỗi sau khi trộn: {chuỗi_kết_quả}")
