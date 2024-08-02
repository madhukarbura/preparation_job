
n=int(input())
arr=list(map(int,input().split()))
sum=0
for choclate in arr:
    sum+=choclate/n
    if choclate%3!=0:
        sum+=1
print(sum)