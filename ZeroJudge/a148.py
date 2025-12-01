import sys
import math
for i, line in enumerate(sys.stdin):
    if not line or line == "" or line == "\n":
        break
    thesum = 0
    count = 0
    x = line.strip().split()
    del x[0]
    for j, val in enumerate(x):
        thesum += int(val)
        count = j+1
    if math.floor(thesum/count+0.5) > 59:
        print("no")
    else:
        print("yes")

        
