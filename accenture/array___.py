n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=list(map(int,input().split()))
for i in arr1:
    if i not in arr2:
        print(i)
for j in arr2:
    if j not in arr3:
        print(j)
"""5
1 2 3 4 5
1 2 4 5
1 4 5
output:3
2"""