def cubesum(n):
    total = 0
    for digit in str(n):
        total += int(digit) ** 3
    return total
def isArmstrong(n):
    return n == cubesum(n)
def PrintArmstrong():
    for num in range(1, 1000):
        if isArmstrong(num):
            print(num)
n = 187
print(f"Tổng các lập phương của các chữ số của {n} là: {cubesum(n)}")
#bai 2
print("Các số Armstrong từ 1 đến 999 là:")
PrintArmstrong()

n = 579
print(f"{n} có phải là số Armstrong không? {isArmstrong(n)}")