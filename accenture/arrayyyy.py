n=int(input())
arr=list(map(int,input().split()))
ar=[]
for i in range(n):
    if arr[i]>=0:
        ar.append(arr[i])
if len(ar)%2==0:
    print(ar[len(ar)//2-1])
    
else:
    print(ar[len(ar)//2])
    
"""5
1 -2 3 -4 5
3"""