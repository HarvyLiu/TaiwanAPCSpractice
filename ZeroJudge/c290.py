theinput = input().strip()
num = int(theinput)
length = len(theinput)-1
oddlist = theinput[0::2]
evenlist = theinput[1::2]
oddsum = 0
evensum = 0
for val in oddlist:
    oddsum += int(val)
for val in evenlist:
    evensum += int(val)
print(abs(oddsum - evensum))
