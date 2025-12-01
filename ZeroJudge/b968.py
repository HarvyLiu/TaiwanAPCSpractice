import sys
theList = []
for line in sys.stdin:
    theList.append(line.strip())
    if line == "" or line == "\n":
        break
    if not line:
        break
print(f"{theList[0]} and {theList[1]} sitting in the tree")
