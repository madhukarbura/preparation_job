m=int(input())
n=int(input())
sum1=0
sum2=0
for i in range(n+1):
    if i % m==0:
        sum1+=i
    else:
        sum2+=i
print(sum2-sum1)