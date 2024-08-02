"""n=int(input())
if n>n and n%2==0:
    print("Yes")
else:
    print("No")
    """
k=int(input())
h=float(input())
bmi=k/h**2
if bmi<10:
    print(0)
elif bmi>=18 and bmi<25:
    print(1)
elif bmi >=25 and bmi <30:
    print(2)
elif bmi >=30 and bmi <40:
    print(3)
else:
    print(4)
#60
#1.75
#output:1