lst = [int(i) for i in input('Enter list: ').split()]
lst2 = []
for i in lst:
	if i not in lst2:
		lst2.append(i)
k = tuple(lst2)
print(k)