n=int(input())
arr=list(map(int,input().split()))
arr.sort()
summ=0
left=0
right=n-1
while left<right:
    summ+=(arr[right]-arr[left])
    left+=1
    right-=1
print(summ)
"""4
1 2 3 4
output=4"""  