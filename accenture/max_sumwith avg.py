n=int(input())
arr=list(map(int,input().split()))
arr.sort()
avg=(arr[-1]+arr[-2])/2
for i in range(n):
    if arr[i]<avg:
        arr[i]=0
print(sum(arr))
#5
#1 2 3 4 5
#out 5