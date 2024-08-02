n=int(input())
str=input()
str1=list(str)
k=int(input())
if n==0:
    print("NULL")
else:
    k=k%n
    print(str[k:]+str[:k])   

"""for i in range(k):
    temp=str1.pop(0)
    str1.append(temp)
print("".join(str1))"""
"""5
abcde
7 rotations firstchar
cdeab"""