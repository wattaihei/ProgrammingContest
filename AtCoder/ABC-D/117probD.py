N, K = map(int, input().split())
A = list(map(int, input().split()))

i = 1
ans = sum(A)
while i <= K:
    b = 0
    for a in A:
        b += a^i
    ans = max(ans, b)
    i *= 2
b = 0
for a in A:
    b += a^K
ans = max(ans, b)
print(ans)
