N = int(input())
A = list(map(int, input().split()))

S = sum(A)

k = 0
ans = int(1E18)
for i, a in enumerate(A):
    if i == N-1:
        break
    k += a
    ans = min(ans, abs(2*k-S))

print(ans)