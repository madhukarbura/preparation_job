def bubble_sort_count(arr):
    count=0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
    return count
n=int(input())
l=[]
for i in range(n):
    m=int(input())
    arr=list(map(int,input().split()))
    l.append(arr)
for i in range(n):
    print(bubble_sort_count(l[i]))