n=int(input())
arr=list(map(int,input().split()))
arr1=list(map(int,input().split()))
res=[]
for i in arr1:
    res.append(arr[i])
print(*res)
"""10 20 30 40 50
4 1 0 2 3
output:50 20 10 30 40"""