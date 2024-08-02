def col_commas(num):
    s=str(num)
    return (len(s)-1)//3
n=int(input())
count=0
for i in range(1000,n+1):
    count+=col_commas(i)
print(count) 
#1000  1
#5000  4001  