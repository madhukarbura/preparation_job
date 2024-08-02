n=input().upper()
count=0
hcount=0
for letter in n:
    if letter =="H":
        count+=2
        hcount+=1
        if hcount==3:
            break
    elif letter=="T":
        count+=-1
        hcount=0
print(count)
#input=HHHTT if consicutive 3 h then print count
#output=6