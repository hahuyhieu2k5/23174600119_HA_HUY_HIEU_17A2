def thao_tac_chuoi(chuoi):
  """
  Hàm thực hiện các thao tác trên chuỗi ký tự.

  Tham số:
    chuoi: Chuỗi ký tự cần thao tác.

  Trả về:
    Từ điển chứa kết quả của các thao tác.
  """
  if len(chuoi) <= 10:
    print("Độ dài chuỗi phải lớn hơn 10 ký tự.")
    return

  ket_qua = {}

  # a) Trích ra chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8
  ket_qua["a"] = chuoi[2:8]

  # b) Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5
  ket_qua["b"] = chuoi[5:10]

  # c) Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự
  ket_qua["c"] = chuoi[-3:]

  # d) Chuyển đổi các ký tự trong chuỗi thành chữ thường
  ket_qua["d"] = chuoi.lower()

  # e) Chuyển đổi các ký tự trong chuỗi thành chữ hoa
  ket_qua["e"] = chuoi.upper()

  # f) Đảo ngược chuỗi ký tự
  ket_qua["f"] = chuoi[::-1]

  return ket_qua

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ")

# Thực hiện các thao tác trên chuỗi
ket_qua = thao_tac_chuoi(chuoi)

# In ra kết quả
if ket_qua:
  for key, value in ket_qua.items():
    print(f"{key}: {value}")
