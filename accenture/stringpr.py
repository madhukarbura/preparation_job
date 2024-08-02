str=input()
stack=[]

for char in str:
    if len(stack)!=0 and stack[-1]==char:
        stack.pop()
    else:
        stack.append(char)
if len(stack)==0:
    print("Empty string")
else:
    print("".join(stack))
    
"""abbac
output=c
baaab
output=bab"""
    
        