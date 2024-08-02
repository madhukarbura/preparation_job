
def xx(dic):
    maxx=0
    maxx_etement=""
    for key,val in dic.items():
        if val >maxx:
            maxx=val
            max_element=key
    return max_element

strr=input()
res=""
vowels=["a","e","i","o","u"]
for i in strr:
    if i in vowels:
        res+=i
dic={}
for item in res:
    if item in dic:
        dic[item]+=1
    else:
        dic[item]=1
print(xx(dic))
