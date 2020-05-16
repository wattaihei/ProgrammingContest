Q = int(input())
data = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    data.append((N, A))

for N, A in data:
    S = sum(A)
    ans = S//N
    if S % N != 0:
        ans += 1
    print(ans)