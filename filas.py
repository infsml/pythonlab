def fislas5(n,k):
    return [i*i for i in range(n,n+5)]+[i*i for i in range(k-4,k+1)]

"""for i in range(n,n+5):
    print(i*i)
for i in range(k-4,k+1):
    print(i*i)
"""
print(fislas5(1,30))

