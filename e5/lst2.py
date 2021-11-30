kst = input("Enter string : ")
upr = []
lwr = []
for i in kst:
	if i.islower():lwr.append(i)
	elif i.isupper():upr.append(i)
print(''.join(upr+lwr))