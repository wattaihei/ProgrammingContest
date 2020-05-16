import sys
input = sys.stdin.readline

N, A, B, K = map(int, input().split())
H = list(map(int, input().split()))

a = 0
P = []
for h in H:
    remain = h%(A+B)
    if remain == 0: remain += A+B
    if 0 < remain <= A:
        P.append(0)
    else:
        P.append((remain-1)//A)
P.sort()
ans = 0
tmp = 0
for p in P:
    if tmp + p <= K:
        tmp += p
        ans += 1
    else:
        break
print(ans)