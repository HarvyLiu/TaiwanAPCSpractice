import sys
for i, line in enumerate(sys.stdin):
    result = 1
    if i == 0:
        continue

    for i, char in enumerate(line.strip()):
        result *= int(line.strip()[i])
    print(result)
