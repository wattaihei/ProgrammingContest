Q = int(input())
data = []
for _ in range(Q):
    A = list(map(int, input().split()))
    data.append(A)

for a, b, c in data:
    ans = 0
    for n in range(b+1):
        if b-n < 0: break
        y = min(n, c//2)*3
        x = min((b-n)//2, a)*3
        ans = max(ans, x+y)
    print(ans)