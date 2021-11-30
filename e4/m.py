k = input("Enter a string : ")
freq = {}
for i in k:
	if i in freq:
		freq[i] += 1
	else:
		freq[i] = 1
print(freq)