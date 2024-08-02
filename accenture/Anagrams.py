input1=input()
input2=input()
input1="".join(sorted(input1))
input2="".join(sorted(input2))
if input1==input2:
    print("Yes")
else:
    print("No")