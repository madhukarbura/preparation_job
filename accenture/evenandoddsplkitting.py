size=int(input())
arr=[]
even=[]
odd=[]
for i in range(size):
    k=int(input())
    arr.append(k)
for i in range(len(arr)):
    if i %2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
even.sort()
odd.sort()
print(even,odd,end="\n")