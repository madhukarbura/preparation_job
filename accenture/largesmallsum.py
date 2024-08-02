arr=list(map(int,input().split()))
even=[]
odd=[]
if len(arr)<=3:
    print(0)
else:
    for i in range(len(arr)):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    print(even[-2]+odd[-2])
#3 2 1 7 5 4
#7 out