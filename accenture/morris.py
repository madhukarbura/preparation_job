def fun(n):
    
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return (fun(n-1)+7*fun(n-2)+n//4)%(10**9+7)
n=int(input())
print(fun(n))
#8
#output:6713