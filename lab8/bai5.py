def sum_of_divisors(n):
    sum_divisors = 0  
    for i in range(1, n // 2 + 1):
        if n % i == 0:          
            sum_divisors += 1   
    return sum_divisors
def are_amicable_numbers(num1, num2):  
    sum1 = sum_of_divisors(num1)
    sum2 = sum_of_divisors(num2)    
    return sum1 == num2 and sum2 == num1
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
if are_amicable_numbers(num1, num2):
    print(f"{num1} và {num2} là số amicable.")
else:
    print(f"{num1} và {num2} không phải là số amicable.")
