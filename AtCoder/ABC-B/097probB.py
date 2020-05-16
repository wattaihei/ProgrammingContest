X = int(input())

ans = 1
for b in range(2, X+1):
    a = X
    c = 0
    while a >= b:
        c += 1
        a = a // b
    if c >= 2:
        ans = max(ans, b**c)
print(ans)