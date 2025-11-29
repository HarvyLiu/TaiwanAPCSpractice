theinput = input()
x = 0
abool = False
for i in range(len(theinput)-1, -1, -1):
    if theinput[x] == theinput[i]:
        abool = True 
    else:
        abool = False
        break
    x += 1
if abool:
    print("yes")
else:
    print("no")
