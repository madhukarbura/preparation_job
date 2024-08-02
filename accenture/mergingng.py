n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr1=list(map(int,input().split()))
arr2=arr+arr1
arr2.sort()
for i in arr2:
    
    print(i)