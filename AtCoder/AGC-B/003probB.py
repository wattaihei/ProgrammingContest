N = int(input())

ans = 0
A = []
for _ in range(N):
    a = int(input())
    ans += a // 2
    if a % 2 == 1:
        A.append(1)
    elif a != 0:
        ans -= 1
        A.append(2)
    else:
        A.append(0)

a1 = 0
for a in A:
    if a > 0:
        a1 += a
    else:
        ans += a1 // 2
        a1 = 0

ans += a1 // 2

print(ans)