the_input = input()
formatted = the_input[0:1]
num_convert = 0
if formatted == "A":
    num_convert = 10
elif formatted == "B":
    num_convert = 11
elif formatted == "C":
    num_convert = 12
elif formatted == "D":
    num_convert = 13
elif formatted == "E":
    num_convert = 14
elif formatted == "F":
    num_convert = 15
elif formatted == "G":
    num_convert = 16
elif formatted == "H":
    num_convert = 17
elif formatted == "I":
    num_convert = 34
elif formatted == "J":
    num_convert = 18
elif formatted == "K":
    num_convert = 19
elif formatted == "L":
    num_convert = 20
elif formatted == "M":
    num_convert = 21
elif formatted == "N":
    num_convert = 22
elif formatted == "O":
    num_convert = 35
elif formatted == "P":
    num_convert = 23
elif formatted == "Q":
    num_convert = 24
elif formatted == "R":
    num_convert = 25
elif formatted == "S":
    num_convert = 26
elif formatted == "T":
    num_convert = 27
elif formatted == "U":
    num_convert = 28
elif formatted == "V":
    num_convert = 29
elif formatted == "W":
    num_convert = 32
elif formatted == "X":
    num_convert = 30
elif formatted == "Y":
    num_convert = 31
elif formatted == "Z":
    num_convert = 33

last_digit = str(num_convert)[-1]
num_calc2 = int(last_digit) * 9 + int(str(num_convert)[0])
input_split = list(the_input[1:])
for i in range(0, len(input_split) - 1):
    num_calc2 += int(input_split[i]) * (8 - i)
num_calc2 += int(input_split[-1])
if num_calc2 % 10 == 0:
    print("real")
else:
    print("fake")

