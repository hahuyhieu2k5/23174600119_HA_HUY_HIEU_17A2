# Nhập dãy số từ người dùng
numbers = input("Nhập dãy số, cách nhau bằng dấu cách: ").split()

# Chuyển đổi các phần tử của dãy từ chuỗi thành số
numbers = [float(num) for num in numbers]

# Tìm số lớn nhất và số nhỏ nhất trong dãy số
max_number = max(numbers)
min_number = min(numbers)

# In ra màn hình số lớn nhất và số nhỏ nhất trong dãy số
print("Số lớn nhất trong dãy là:", max_number)
print("Số nhỏ nhất trong dãy là:", min_number)
