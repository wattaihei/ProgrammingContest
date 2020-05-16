N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
d = 0
if A[0] > X:
    d = A[0] - X
    ans += d
for i in range(N-1):
    s = A[i]+A[i+1]-d
    if s > X:
        d = s - X
        ans += d
    else:
        d = 0
 
print(ans)