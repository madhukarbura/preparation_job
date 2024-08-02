n=input().lower()
r=""
m="abcdefghijklmnopqrstuvwxyz"
for letter in m:
    if letter not in n:
        r+=letter
        
print(r)