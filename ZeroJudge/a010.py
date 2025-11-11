num = int(input())
original = num
factors = {}
i = 2

# prime factorization
while i * i <= num:
    while num % i == 0:
        num //= i
        factors[i] = factors.get(i, 0) + 1
    i += 1

if num > 1:
    factors[num] = factors.get(num, 0) + 1

# formatting
parts = []
for prime, exp in factors.items():
    if exp == 1:
        parts.append(f"{prime}")
    else:
        parts.append(f"{prime}^{exp}")

print(f"{' * '.join(parts)}")

