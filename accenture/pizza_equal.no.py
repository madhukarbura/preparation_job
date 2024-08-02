N,y=map(int,input().split())
sum=0
while True:
    if N%y==0:
        break
    y+=1
while y>0:
        
    digit=y%10
    sum+=digit
        
    y=y//10


print(sum)
"""100 17
2 out"""