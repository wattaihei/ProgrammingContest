v = [1, 2]
ans = 2
while True:
    a = v[-1] + v[-2]
    if a > 50:
        break
    if a % 2 == 0:
        ans += a
    v.append(a)
print(ans)