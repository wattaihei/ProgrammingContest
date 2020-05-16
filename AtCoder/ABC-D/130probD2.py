N, K = map(int, input().split())
A = list(map(int, input().split()))

s = A[0]
l = 0
r = 0
ans = 0
while l < N:
    if s >= K:
        ans += N-r
        s -= A[l]
        l += 1
    elif r < N-1:
        r += 1
        s += A[r]
    else:
        if s >= K:
            ans += 1
        s -= A[l]
        l += 1
print(ans)