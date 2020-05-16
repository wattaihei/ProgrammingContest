N, A, B = map(int, input().split())
ans = 0
for n in range(1, N+1):
    m = sum([int(c) for c in list(str(n))])
    if A <= m <= B:
        ans += n
print(ans)