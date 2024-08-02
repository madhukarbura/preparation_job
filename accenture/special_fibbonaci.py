"""def fibbspecial(n):
    
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return (fibbspecial(n-1)*fibbspecial(n-1)+fibbspecial(n-2)*fibbspecial(n-2))%47
n=int(input())
print(fibbspecial(n))
"""
n=int(input())
fib=[0]*(n+1)
fib[0]=1
fib[1]=1
for i in range(2,n+1):
    fib[i]=(fib[i-1]*fib[i-1]+fib[i-2]*fib[i-2])%47
print(fib[n])
"""4
29"""