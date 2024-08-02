arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
count=0
for i in range(len(arr)):
    if abs(arr[i]-num)<=diff:
        count+=1
        
print(count)
"""for number 13 with diff 2 the closest are 12 13 14"""