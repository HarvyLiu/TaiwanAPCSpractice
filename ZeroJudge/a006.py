import math
a, b, c = map(int, input().split())

o = (-b+(b**2-4*a*c)**0.5)/(2*a)
p = (-b-(b**2-4*a*c)**0.5)/(2*a)
if b**2-4*a*c < 0:
    print("No real root")
elif b**2-4*a*c == 0:
    print(f"Two same roots x={math.floor(o)}")
elif b**2-4*a*c > 0:
    print(f"Two different roots x1={round(o)} , x2={round(p)}")
