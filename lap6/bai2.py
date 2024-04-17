def is_prime(num):
  """
  Kiểm tra số nguyên dương `num` có phải là số nguyên tố hay không.

  Args:
    num: Số nguyên dương cần kiểm tra.

  Returns:
    True nếu `num` là số nguyên tố, False nếu không.
  """
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def is_perfect(num):
  """
  Kiểm tra số nguyên dương `num` có phải là số hoàn hảo hay không.

  Args:
    num: Số nguyên dương cần kiểm tra.

  Returns:
    True nếu `num` là số hoàn hảo, False nếu không.
  """
  if num <= 1:
    return False
  sum_of_divisors = 0
  for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
      if num // i == i:
        sum_of_divisors += i
      else:
        sum_of_divisors += i
        sum_of_divisors += num // i
  return sum_of_divisors == num

n = int(input("Nhập số lượng phần tử trong mảng: "))
arr = []
for i in range(n):
  arr.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

print("Số nguyên tố trong mảng:")
for num in arr:
  if is_prime(num):
    print(num)

print("Số hoàn hảo trong mảng:")
for num in arr:
  if is_perfect(num):
    print(num)
