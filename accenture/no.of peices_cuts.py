def cuts(n):
    sum=1
    for i in range(n+1):
        sum+=i
    return sum
n=int(input())
print(cuts(n))
#else  (n(n+1)/2)+1  sum of n natural numbers+1