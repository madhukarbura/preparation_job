n=int(input())
p=int(input())
timeleft=240-p
problem_solved=0
i=1
while True:
    timeleft-=5*i
    if timeleft<0:
        break
    problem_solved+=1
    i+=1
    
print(problem_solved)