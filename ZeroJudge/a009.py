shift = 7
text = input()
result = ""
count = 0
for letter in text:
    uncrypted = chr(ord(text[count])-shift)
    count += 1
    result += uncrypted
print(result)
