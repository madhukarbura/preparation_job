def max_frequency(m):
    frq_dict={}
    for item in m:
        if item in frq_dict:
            frq_dict[item]+=1
        else:
            frq_dict[item]=1
    max_frequency=-1
    max_element=None
    multiple_max=False
    for key, value in frq_dict.items():
        if value > max_frequency:
            max_frequency=value
            max_element=key
            multiple_max=False
        elif value == max_frequency:
            multiple_max=True
    if multiple_max:
        return -1
    else:
        return max_element
    
n=int(input())
m=list(map(int,input().split()))
result=max_frequency(m)
print(result)
        