a = str(input('введите строку'))
for b in range(len(a)):
    if b % 2 == 0:
        print(a[b].upper())
    else:
        print(a[b])