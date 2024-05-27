def sumPdivisors(n):
    sum_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:   
            sum_divisors += i
    return sum_divisors
n = int(input("Nhập một số để tìm tổng các ước số chính: "))
print(f"Tổng các ước số chính của số {n} là: {sumPdivisors(n)}")
