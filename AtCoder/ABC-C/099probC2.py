N = int(input())
ans = N
for n9 in range(N//9+1):
    a = N - 9*n9
    if a < 0:
        continue
    c = 0
    while a >= 6:
        c += a % 6
        a = a // 6
    c2 = 0
    while n9 >= 9:
        c2 += n9 % 9
        n9 = n9 // 9
    cost = a + c + c2 + n9
    ans = min(ans, cost)
print(ans)