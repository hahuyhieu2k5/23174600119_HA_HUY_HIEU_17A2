# Nhập số lượng phần tử của mảng
n = int(input("Nhập số lượng phần tử của mảng: "))
    
# Khởi tạo mảng
arr = []

# Nhập các phần tử của mảng từ người dùng
print("Nhập các phần tử của mảng:")
for i in range(n):
    num = int(input(f"Phần tử thứ {i + 1}: "))
    arr.append(num)

# Tính tổng các số chẵn và tổng các số lẻ
sum_even = 0
sum_odd = 0
for num in arr:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

# In kết quả
print("Tổng các số chẵn trong mảng là:", sum_even)
print("Tổng các số lẻ trong mảng là:", sum_odd)