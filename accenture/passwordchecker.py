input=input()
cap=0
num=0
space=0
if len(input)<4 or (input[0]==0 and input[0]==9):
    print(0)
else:
    for i in range(len(input)):
        if input[i].isupper():
            cap+=1
        elif input[i].isdigit():
            num+=1
        elif input[i]==" " or input[i]=="/":
            space+=1
if cap>0 and num>0 and space==0:
    print(1)
else:
    print(0)            