import random

x = range(1,101)

grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
chosen = []
def pg(n):
    if n %10==0:
        grid[int(n//10)-1][9]=n
    else:
        grid[int(n//10)][(n%10)-1] = n
    for i in range(0,10):
        for j in range(0,10):
            print(grid[i][j],end="    ")
        print("")
        print("")
def ran():
    n = random.choice(x)
    if n not in chosen:
        chosen.append(n)
        print("your NUMBER is: ",n)
        pg(n)
    else:
        ran()


        
n=1
while n!=0:
    ran()
    print("enter 1 tochoose again and 0 to stop")
    n = int(input())
    
