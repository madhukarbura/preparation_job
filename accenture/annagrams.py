input1=input().lower()
input2=input().lower()
in1="".join(sorted(input1))
in2="".join(sorted(input2))
#list to string="".join(listname)
if in1==in2:
    print("Yes")
else:
    print("No")
    
