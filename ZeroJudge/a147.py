import sys

for line in sys.stdin:
    res = ""
    if not line or line == "" or line == "\n" or int(line) == 0:
        break
    for i in range(int(line)):
        if (i+1)%7 != 0 and i!=0 and i+1 < int(line):
            res += f" {i+1}"
        elif i == 0:
            res = f"{i+1}"
        else:
            continue
    print(res)
