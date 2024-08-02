def rat_food(rats,unit,n,arr):
    sum=0
    number=rats*unit
    for i in range(n):
        sum=sum+arr[i]
        if sum>=number:
            return i+1
    return 0
rats=int(input())
unit=int(input())
n=int(input())
arr=list(map(int,input().split()))
print(rat_food(rats,unit,n,arr))
