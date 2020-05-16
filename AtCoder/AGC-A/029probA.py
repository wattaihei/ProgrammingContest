
seq = 0
ans = 0
for i, s in enumerate(list(input())):
    if s == 'W':
        seq += 1
        ans += i + 1 - seq
print(ans)
