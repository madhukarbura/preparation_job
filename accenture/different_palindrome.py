n=int(input())
while (str(n)!=str(n)[::-1]):
    n=n+int(str(n)[::-1])
print(n)
"""28
121"""