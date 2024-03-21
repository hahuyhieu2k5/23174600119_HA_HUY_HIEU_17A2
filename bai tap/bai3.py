# em không biết làm bài này ạ em tham khảo thôi ạ
# Tạo một dictionary để ánh xạ các chữ số thành từ tiếng Anh
chu_so = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

# Tạo một dictionary riêng cho các số từ 10 đến 19
chu_so_10_den_19 = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

# Tạo một dictionary riêng cho các số hàng chục từ 20 đến 90
chu_so_hang_chuc = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

# Nhập số nguyên có ba chữ số từ người dùng
so_nguyen = int(input("Nhập vào một số nguyên có ba chữ số: "))

# Kiểm tra xem số nguyên có đúng ba chữ số không
if 100 <= so_nguyen <= 999:
    hang_tram = so_nguyen // 100
    hang_chuc = (so_nguyen % 100) // 10
    hang_don_vi = so_nguyen % 10

    doc_hang_tram = chu_so[hang_tram] + " hundred " if hang_tram != 0 else ""
    if hang_chuc == 1:
        doc_hang_chuc = chu_so_10_den_19[so_nguyen % 100] + " "
        doc_hang_don_vi = ""
    else:
        doc_hang_chuc = chu_so_hang_chuc[hang_chuc] + " " if hang_chuc != 0 else ""
        doc_hang_don_vi = chu_so[hang_don_vi] if hang_don_vi != 0 else ""

    doc_so = doc_hang_tram + doc_hang_chuc + doc_hang_don_vi
    print("Cách đọc của số nguyên", so_nguyen, "là:", doc_so.strip())
else:
    print("Số nguyên bạn nhập không có ba chữ số!")