strr=input()
j=2
sum=int(strr[0])
for i in range(1,len(strr)-1,2):
    if strr[i]=="C":
        sum^=int(strr[j])
        j+=2
    elif strr[i]=="A":
        sum=sum&int(strr[j])
        j+=2
    else:
        sum=sum| int(strr[j])
print(sum)