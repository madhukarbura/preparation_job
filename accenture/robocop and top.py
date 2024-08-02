X,N,Y,M=map(int,input().split())
"""l=[]
m=[]
for i in range(max(N,M)):
    l.append(X+N)
    m.append(Y+M)
    X=X+N
    Y=Y+M
for li in l:
    if li in m:
        print(li)"""
r=0
while True:
    s=(X+r*N-Y)/M
    if s-int(s)==0:
        break
    r+=1
print(X+r*N)
#input=3 5 2 7
#expplanation 3+5=8  8+5=13 18 23 ... and y= 2+7=9 9+7=16  23  30....
#ountput=23   at 23 sec they meet together