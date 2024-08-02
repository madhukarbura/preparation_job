def selection_sort_count(arr):
    count=0
    for i in range(len(arr)):
        minn=i
        for j in range(i+1,len(arr)):
            
            if arr[j]<arr[minn]:
                minn=j
        if minn!=i:
            arr[i],arr[minn]=arr[minn],arr[i]
            count+=1
    return count
n=int(input())
l=[]
for i in range(n):
    m=int(input())
    arr=list(map(int,input().split()))
    l.append(arr)
for i in range(n):
    print(selection_sort_count(l[i]))
"""2
3
4 2 5
5
10 11 8 7 1
out:
1
3"""