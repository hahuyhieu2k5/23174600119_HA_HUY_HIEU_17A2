# Nhập dãy số từ người dùng
sequence = input("Nhập dãy số, cách nhau bằng dấu cách: ").split()

# Chuyển đổi các phần tử của dãy từ chuỗi thành số nguyên
sequence = [int(num) for num in sequence]

# Kiểm tra xem dãy số có tạo thành cấp số cộng không
if len(sequence) < 3:
    print("Dãy số không đủ phần tử để tạo thành cấp số cộng.")
else:
    difference = sequence[1] - sequence[0]
    is_arithmetic_progression = all(sequence[i + 1] - sequence[i] == difference for i in range(1, len(sequence) - 1))

    # In kết quả
    if is_arithmetic_progression:
        print("Dãy số", sequence, "tạo thành cấp số cộng.")
    else:
        print("Dãy số", sequence, "không tạo thành cấp số cộng.")
