"""n=int(input())
sum=0
for i in range(n):
    for j in range(i+1,0,-1):
        sum+=j
    for k in range(i+1,1,-1):
        sum+=k
print(sum)"""
n=int(input())
sum=0
res=n
num=2
for i in range(n-1,0,-1):
    res+=2*i*num
    num+=1
print(res)
"""3
output:
17
1+
2+1+2+
3+2+1+2+3"""