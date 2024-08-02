str=input()
key=[0,1,2,3,4,5,6,7,8,9,00]
count=0
i=0
while i<(len(str)):
    if int(str[i:i+2]) == 00:
        count+=1
        i=i+2
    elif int(str[i]) in key:
        count+=1
        i+=1
print(count)
#100
#output=2  1 00 there are 2 count
#key will be provided in description