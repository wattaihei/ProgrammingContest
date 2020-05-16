H = int(input())

now = 1
ans = 0
while H > 0:
    ans += now
    H //= 2
    now *= 2

print(ans)