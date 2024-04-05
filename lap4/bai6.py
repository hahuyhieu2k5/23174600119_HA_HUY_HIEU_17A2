so_chu_so = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}
while True:
    so_nhap = input("Nhập một số từ bàn phím: ")
    ket_qua = ''
    for chu_so in so_nhap:
        if chu_so in so_chu_so:
            ket_qua += so_chu_so[chu_so] + ' '
        else:
            print("Số không hợp lệ.")
            break
    else:
        print("Kết quả in ra màn hình:", ket_qua)