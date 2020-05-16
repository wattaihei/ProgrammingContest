s = int(input())

i = 1
a = [s]
while True:
    i += 1
    n = a[-1]
    if n % 2 == 0:
        next = n // 2
    else:
        next = 3 * n + 1
    if next in a:
        break
    else:
        a.append(next)

print(i)