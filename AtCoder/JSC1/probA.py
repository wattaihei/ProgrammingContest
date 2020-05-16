M, D = map(int, input().split())

ans = 0
for m in range(1, M+1):
    for i in range(1, 10):
        if m%i == 0 and i >= 2:
            k = m//i
            if 2 <= k <= 9 and 10*i+k <= D:
                ans += 1
print(ans)