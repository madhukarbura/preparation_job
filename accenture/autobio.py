def is_autobiographical(n: str) -> bool:
    count = [0] * 10
    for digit in n:
        count[int(digit)] += 1
    
    for i in range(len(n)):
        """[1,2,1,0,0,0,0,0,0,0]"""
        if count[i] != int(n[i]):
            return False
    return True

def find_position_of_autobiographical(n: str) -> int:
    if is_autobiographical(n):
        return len(n) - 1
    else:
        return -1

# Test cases
n=input()
print(find_position_of_autobiographical(n))
#1210 input out=3