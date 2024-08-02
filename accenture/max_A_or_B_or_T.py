n=int(input())
arr=list(map(int,input().split()))
uniq=set(arr)
A,B=0,0
for  num in uniq:
    if num%2==0:
        if arr.count(num)%2==0:
            A+=1
        else:
            B+=1
    else:
        if arr.count(num)%2==0:
            B+=1
        else:
            A+=1
if A>B:
    print("A",A-B)
elif B>A:
    print("B",B-A)
else:
    print("T",0)

#6
#1 2 2 3 4 4
#A 4