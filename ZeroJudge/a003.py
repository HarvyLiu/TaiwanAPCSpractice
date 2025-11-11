MD = input("輸入資料共一行，包含兩個整數，分別為月份及日期").split()
S = (int(MD[0]*2) + int(MD[1]))%3
#match S:                    doesn't work in that platform because it uses 3.8 instead of 3.10 or higher
#    case 0:
#        print("普通")
#    case 1:
#        print("吉")
#    case 2:
#        print("大吉")
#    case _:
#        print("WTF")

if S == 0:
    print("普通")
elif S ==1:
    print("吉")
elif S ==2:
    print("大吉")
else:
    print("WTF")
