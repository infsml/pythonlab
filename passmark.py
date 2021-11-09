k = input('Enter string ')
lo,up,dig,spec = [0]*4
for i in k:
    if i.islower() : lo += 1
    elif i.isupper() : up += 1
    elif i.isdigit() : dig += 1
    else : spec += 1
print(f'lower {lo}, upper {up}, digit {dig}, special char {spec}')
if len(k) < 16 and len(k) > 10 :
    print('password is valid')
else :
    print('password is invalid')
