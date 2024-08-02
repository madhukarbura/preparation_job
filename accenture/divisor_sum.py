n=int(input())
summ=0
for i in range(1,n+1):
    if n%i==0:
        summ+=i
print(summ)
#input 6  (1,2,3,6) are divisors of 6 so sum of all =12