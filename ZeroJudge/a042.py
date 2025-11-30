import sys 

d = 2

for line in sys.stdin:
    if line == "\n":
        break
    n = int(line)
    a = 2
    for i in range(n-1):
        a += d*(i+1)
    print(a)
    
    
