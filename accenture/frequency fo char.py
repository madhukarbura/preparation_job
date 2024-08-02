def frequency(dic,str,chr):
    maxx=0
    max_element=max(dic,key=dic.get)
    """for key,val in dic.items():
        if val>maxx:
            maxx=val
            max_element=key"""
    res=""
    for i in range(len(str)):
        if str[i]==max_element:
            res+=chr
        else:
            res+=str[i]
    return res       
str=input()
chr=input()
dic={}
for item in str:
    if item in dic:
        dic[item]+=1
    else:
        dic[item]=1
result=frequency(dic,str,chr)
print(result)