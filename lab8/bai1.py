def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def tim_so_nguyen_to_sinh_doi(max):
    so_nguyen_to_sinh_doi = []
    for i in range(2, max - 1):
        if kiem_tra_so_nguyen_to(i) and kiem_tra_so_nguyen_to(i + 2):
            so_nguyen_to_sinh_doi.append((i, i + 2))
    return so_nguyen_to_sinh_doi
max = 1000
so_nguyen_to_sinh_doi = tim_so_nguyen_to_sinh_doi(max)
print("Các cặp số nguyên tố sinh đôi nhỏ hơn 1000 là:")
for so in so_nguyen_to_sinh_doi:
    print(so)