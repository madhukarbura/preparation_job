n=int(input())
k=1
for i in range(n+1):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()
