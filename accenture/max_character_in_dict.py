str=input()
d={}
for item in str:
    if item in d:
        d[item]+=1
    else:
        d[item]=1
print(max(d,key=d.get))
        