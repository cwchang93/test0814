#def C(n, r):
#    if r == 0:
#         return 1
#    if r == n:
#         return 1
#    return C(n-1, r) + C(n-1, r-1)
def combination(n,r):
    c = 1
    k = 1
    for i in range(n,r,-1):
        c = c*i/k
        k = k+1
    return(c)

print(combination(900,40))
