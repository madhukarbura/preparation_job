

def prime(n):
    if n<2:
        return False
    for j in range(2,(n//2)+1):
        if n%j==0:
            return False
n=int(input())
while True:
    n=n+1
    if prime(n):
        break
print(n)

    