"""a=int(input())
print(bin(a))
print(type(bin(a)))
n=input()
print(int(n,2))"""
n=int(input())
res=""
while n>0:
    res+=str(n%2)
    n=n//2
res=res[::-1]
print(res)
j=0
sum=0
for i in range(len(res)-1,-1,-1):
    sum+=int(res[i])*(2**j)
    j+=1
print(sum)


    