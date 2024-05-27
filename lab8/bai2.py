def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * tinh_giai_thua(n - 1)
def hoan_vi(n, r):
    return tinh_giai_thua(n) / tinh_giai_thua(n - r)

def to_hop(n, r):
    return hoan_vi(n, r) / tinh_giai_thua(r)
n = 5
r = 3
so_hoan_vi = hoan_vi(n, r)
so_to_hop = to_hop(n, r)

print(f"Số hoán vị của {n} phần tử lấy {r} phần tử là: {int(so_hoan_vi)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử là: {int(so_to_hop)}")
