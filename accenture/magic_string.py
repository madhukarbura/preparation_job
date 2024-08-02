def magic_string(str):
    dic={}
    for i in str:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    maxx=0
    max_element=""
    for key,val in dic.items():
        if val>maxx:
            maxx=val
            max_element=key
    return abs(maxx-len(str))
str=input()
print(magic_string(str))
"""aabbccdddd
6 max is d and number of d - len or how many steps to change to d all characters

not relatedto above
max(d.values()) function"""