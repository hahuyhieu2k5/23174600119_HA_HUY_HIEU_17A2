def tim_lcs(str1, str2):
  """
  Hàm tìm chuỗi con chung ngắn nhất của hai chuỗi ký tự.

  Tham số:
    str1: Chuỗi ký tự thứ nhất.
    str2: Chuỗi ký tự thứ hai.

  Trả về:
    Chuỗi ký tự con chung ngắn nhất của hai chuỗi.
  """
  len_str1 = len(str1)
  len_str2 = len(str2)

  # Tạo bảng DP
  dp = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]

  # Khởi tạo bảng DP
  for i in range(len_str1 + 1):
    for j in range(len_str2 + 1):
      if i == 0 or j == 0:
        dp[i][j] = 0
      elif str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  # Truy ngược bảng DP để tìm LCS
  i = len_str1
  j = len_str2
  lcs = ""
  while i > 0 and j > 0:
    if str1[i - 1] == str2[j - 1]:
      lcs = str1[i - 1] + lcs
      i -= 1
      j -= 1
    else:
      if dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
      else:
        j -= 1

  return lcs

# Nhập hai chuỗi ký tự từ người dùng
str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")

# Tìm chuỗi con chung ngắn nhất
lcs = tim_lcs(str1, str2)

# In ra kết quả
print(f"Chuỗi con chung ngắn nhất của '{str1}' và '{str2}' là: '{lcs}'")
