n=int(input())
sum_fact=1
for i in range(2,n//2+1):
    if n%i==0:
        sum_fact+=i
if sum_fact==n:
    print(1)
else:
    print(sum_fact)
"""6
1"""