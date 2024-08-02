n=int(input())
k=int(input())
arr=list(map(int,input().split()))
max_score=-float("inf")
for i in range(n-k+1):
    temp=arr[i:k+i]
    score=0
    for j in range(k):
        score+=(j+1)*temp[j]
    max_score=max(max_score,score)
print(max_score)
"""5
2
1 2 3 4 5
14 output"""