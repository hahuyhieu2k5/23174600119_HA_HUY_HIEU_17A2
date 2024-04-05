###a
i = 2
while i < 100:
  check = True
  j = 2
  while j <= i // 2:
    if i % j == 0:
      check = False
      break
    j += 1
  if check:
    print(i, end=" ")
  i += 1

  ###b
  i = 1
while i * i < 100:
  print(i * i, end=" ")
  i += 1


  ##c
  a, b = 0, 1
while b < 1000:
  print(b, end=" ")
  a, b = b, a + b