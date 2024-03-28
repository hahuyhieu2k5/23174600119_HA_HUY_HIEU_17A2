1#
for num in range(100, 1002):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print("So nguyen to tu 100 toi 1001 la: ", num)
2#
for num in range(1, 1001):
    if num**0.5 == int(num**0.5):
        print("So chinh phuong tu 1 toi 1000 la: ", num)
3#
fib_sequence = [0, 1] 
for i in range(2, 100):
    next_number = fib_sequence[i-1] + fib_sequence[i-2]
    if next_number >= 100: break
    fib_sequence.append(next_number)
print("Chuỗi Fibonacci số cuối cùng nhỏ hơn 100 là:", fib_sequence)