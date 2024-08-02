def max_frequency(arr):
    dic={}
    for item in arr:
        if item in dic:
            dic[item]+=1
        else:
            dic[item]=1
    maxx=0
    max_element=0
    for key,val in dic.items():
        if val>maxx:
            maxx=val
            max_element=key
    return max_element
n=int(input())
list1=[]
for i in range(n):
    m=int(input())
    arr=list(map(int,input().split()))
    
    list1.append(arr)
for i in range(n):
    print(max_frequency(list1[i]))
"""
input:
3
7
2 4 5 2 3 2 4
6
1 2 1 1 2 1
10
1 1 1 1 1 1 1 1 1 1
out:
2
1
1
"""