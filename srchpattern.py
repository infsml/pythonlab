i1 = input("Enter string ")
i2 = input("Enter pattern ")
i3 = i1.casefold()
i4 = i2.casefold()
n = 0
for i in range(len(i3)):
    for j in range(len(i4)):
        if i3[i+j] != i4[j]:break
    else: n += 1
print(n)
