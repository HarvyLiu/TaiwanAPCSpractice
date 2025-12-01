theinput = int(input())
i = 0
score = 0
def thefunc(theinput):
    count = 0
    global score
    for _ in range(theinput+1):
        if count>0 and count <= 10:
            score += 6;
        if count > 10 and count <= 20: 
            score += 2

        if count > 20 and count <= 40:
            score += 1

        count += 1
thefunc(theinput)
print(score)

