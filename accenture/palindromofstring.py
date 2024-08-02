string=input()
flag=0
for i in range(len(string)//2):
    if string[i]!=string[len(string)-i-1]:
        flag=1
if flag==1:
    print(0)
else:
    print(1)
    