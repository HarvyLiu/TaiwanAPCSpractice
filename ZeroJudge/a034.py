import sys
alist = []
for line in sys.stdin:
    try:
        alist.append(bin(int(line.strip()))[2:])
    except:
        break
for item in alist:
    print(item)


