x=int(input())
y=int(input())
while y>0:
    if x<y:
        x,y=y,x
    else:
        t=x-y
        x=y
        y=t
print(x)

"""48
        18
        out=6"""