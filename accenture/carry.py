n=int(input())
m=int(input())
count=0
carry=0
N=str(n)
M=str(m)

maxx=max(len(N),len(M))
N=N.zfill(maxx)
M=M.zfill(maxx)
print(N,M)
for i in range(maxx-1,-1,-1):
    
    if (int(N[i])+int(M[i])+carry)>9:
        count+=1
        carry+=1
    else:
        carry=0
    
    
print(count)