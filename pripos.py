def prin_pos(a,b):
    if b<0: return
    if a<0: a=0
    print(list(range(a,b+1)))

prin_pos(int(input("Enter 1st num ")),int(input("Enter 2nd num ")))
