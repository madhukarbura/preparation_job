str1=input()
ch1=input()
ch2=input()
res=""
for i in range(len(str1)):
    if str1[i] ==ch1:
        res+=ch2
    elif str1[i]==ch2:
        res+=ch1
    else:
        res+=str1[i]
print(res)