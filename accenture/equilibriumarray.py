def fun(n,arr):
    eq=0
    for i in range(1,n-1):
        if sum(arr[:i])==sum(arr[i+1:]):
            eq=i+1
            break
    if eq==0:
        return "NOT FOUND"
    else:
        return eq
n=int(input())
arr=list(map(int,input().split()))
print(fun(n,arr))
"""5
2 4 7 3 3   2+4 =6 and 3+3 =6 and print(3) becaue at 3 element the splited equally
3"""