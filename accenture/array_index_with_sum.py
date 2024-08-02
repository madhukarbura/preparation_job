arr=list(map(int,input().split()))
n=int(input())
"""l=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==n:
            l.append(i)
            l.append(j)
print(l)"""
dic={}
res=[]
for i in range(len(arr)):
    ext=n-arr[i]
    if ext in dic:
        res.append(dic[ext])
        res.append(i)
        break
    dic[arr[i]]=i
print(res) 
    
"""1 2 3 4
4
output:[0, 2]"""