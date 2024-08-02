arr=list(map(int,input().split()))
res=""
for i in range(len(arr)):
    while arr[i]>0:
        res+=str(arr[i]%10)
        arr[i]=arr[i]//10
res=list(res)
res.sort(reverse=True)
res="".join(res)
print(int(res))