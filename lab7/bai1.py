
N = int(input("Nhập vào một số nguyên N: "))
if N <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    HH_HIEU = {}
    for x in range(1, N+1):
        HH_HIEU[x] = x**3
    print("Từ điển Hiếu dạng key = x và value = x^3:")
    print(HH_HIEU)

