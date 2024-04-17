################### a
# Nhập số lượng số Fibonacci muốn tạo
n = int(input("Nhập số lượng số Fibonacci muốn tạo: "))

# Danh sách Fibonacci ban đầu
fib_list = [0, 1]

# Sử dụng list comprehension để tạo danh sách Fibonacci
[fib_list.append(fib_list[-1] + fib_list[-2]) for _ in range(2, n)]

# In danh sách Fibonacci ra màn hình
print("Danh sách Fibonacci gồm", n, "số đầu tiên là:")
print(fib_list[:n])



##### b
# Sử dụng list comprehension để tạo danh sách số nguyên tố nhỏ hơn 100
# Danh sách số nguyên tố nhỏ hơn 100 sử dụng list comprehension
primes = [num for num in range(2, 100) if is_prime(num)]

# Hàm kiểm tra số nguyên tố (đã định nghĩa ở trên)
def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

print(primes)
