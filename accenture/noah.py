def noah(n,arr):
    for i in range(n):
        for j in range(n):
            if arr[i]>arr[j] and arr[i]+arr[j]==18:
                return ([arr[i],arr[j]])
    return []
n=int(input())
arr=list(map(int,input().split()))
print(noah(n,arr))

   


"""7
11 12 8 10 11 9 8
output:[10,8]"""