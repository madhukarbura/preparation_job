def convert_to_base(N,num):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res=[]
    while num>0:
        rem=num%N
        res.append(digits[rem])
        num//=N
    return "".join(res[::-1])
N=int(input())
num=int(input())
result=convert_to_base(N,num)
print(result)
#12
#718
#4BA