import sys

for line in sys.stdin:
    count = 0
    if not line or line == "\n" or line == "":
        break
    theList = line.strip().split()
    theList = list(map(int, theList))
    if theList[1] > 0 and theList[1] < theList[0]:
        break
    if theList[1] < 0 and theList[0] < theList[1]:
        break
    while True:
        count += 1
        theList[0] += theList[0] + count
        if theList[0] > theList[1]:
            print(count+1)
            break
