import sys
n = 0
global result
result = ""
thedict = {"0101":"A", "0111":"B", "0010":"C", "1101":"D", "1000":"E", "1110":"F"}
for i, line in enumerate(sys.stdin):
    if not line or line == "" or line == "\n":
        break
    if len(line.strip()) == 1:
        n = int(line)
        continue
    for _ in range(n):
        code = line.strip().replace(" ", "")
        charc = thedict.get(code)
        result += charc
        
    print(result)
