t = int(input())
for _ in range(t):
    a1, a2, a3, a4 = map(int, input().split())

    if a2 - a1 == a3 - a2 == a4 - a3:
        d = a2 - a1
        a5 = a4 + d
    else:
        r = a2 // a1
        a5 = a4 * r

    print(a1, a2, a3, a4, a5)

