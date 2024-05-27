van_ban = "I love wild animals. In cities only place to see them is zoo. Last week I got a chance to visit zoo when my elder brother planned a picnic along with his two friends. We reached there at 10 am. Zoo was divided into many sections like apes, birds, reptiles, butterflies, beast of prey etc. We tried to cover each section. But once we entered the birds section, we lost so much that we spent many hours there. We could hardly cover half section. By the evening we were very tired. We came out and took some snacks. Sweet memory of that day is still fresh in my mind."
tu_dien = {}
for tu in van_ban.split():
    tu = tu.strip('.,').lower()
    tu_dien[tu] = tu_dien.get(tu, 0) + 1
print("Số lượng từ giống nhau trong văn bản:")
for tu, so_luong in tu_dien.items():
    print(f"{tu}: {so_luong}")
tu_nhieu_nhat = max(tu_dien, key=tu_dien.get)
tu_it_nhat = min(tu_dien, key=tu_dien.get)
print("Từ có số lượng nhiều nhất:", tu_nhieu_nhat)
print("Từ có số lượng ít nhất:", tu_it_nhat)