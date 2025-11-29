theinput = input()
flipped = theinput[::-1]
corrected = ""
for i, char in enumerate(flipped):
    if char == "0":
        corrected = flipped[i::1]
    else:
        corrected = flipped[i::1]
        break
if corrected == "":
    corrected = "0"
elif int(corrected) == 0:
    corrected = "0"
print(corrected)
