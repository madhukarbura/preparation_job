n=int(input())
arr=list(map(int,input().split()))
arr.sort()
arr=set(arr)
arr=list(arr)
n=len(arr)
if n<2:
    print(-1)
else:
    print(arr[n-2])