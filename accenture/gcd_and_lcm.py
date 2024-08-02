def gcd(n,m):
    if m==0:
        return n
    else:
        return gcd(m,n%m)
def lcm(n,m):
    return int((n*m)/(gcd(n,m)))
n,m=map(int,input().split())
print(gcd(n,m))
print(lcm(n,m))
"""import math
print(math.gcd(a,b))
print((n*m)//math.gcd(n,m))"""