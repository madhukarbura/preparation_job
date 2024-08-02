def productsmallpair(sum,arr):
    arr.sort()
    if len(arr)<=2 or arr==None:
        return -1
    
    else:
        for i in range(len(arr)-1):
            if arr[i]+arr[i+1]<sum:
                return arr[i]*arr[i+1]
        return 0
sum=int(input())
arr=list(map(int,input().split()))
result=productsmallpair(sum,arr)
print(result)
#9
#5 4 2 3 9 1 7
#out=2