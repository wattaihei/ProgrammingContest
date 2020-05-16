N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

vc = [V[i]-C[i] for i in range(N)]
vc.sort(reverse=True)

ans = 0
for v in vc:
    if v < 0:
        break
    ans += v
print(ans)