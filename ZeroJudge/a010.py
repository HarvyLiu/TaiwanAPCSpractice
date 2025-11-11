num = int(input())
i = 1
list = []
k = 0
string1 = ""
string2 = ""
while True:
    if num > 1:
        i += 1
        if num % i == 0:
            num /= i
            list.append(i)
            i = 0
        else:
            continue
    elif num == 1:
        break
for j in list:
    for list[j] in list:
        k += 1
        string2 = f"{list[j]}^k"
    string1 += string2
