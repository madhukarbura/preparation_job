def fibonaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
def printing_sum(m,n):
    sum=0
    for i in range(m,n,1):
        ans=fibonaci(i)
        sum+=ans
    return sum
m=int(input())
n=int(input())
print(printing_sum(m,n))