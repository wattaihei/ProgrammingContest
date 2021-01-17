import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

T = [[] for _ in range(N+1)]
for i in range(1, N+1):
    j = i*2
    while j <= N:
        T[j].append(i)
        j += i

ans = [0] + A
P = []
for i in reversed(range(1, N+1)):
    a = ans[i]
    if a:
        for t in T[i]:
            ans[t] ^= 1
        P.append(str(i))

print(len(P))
print(" ".join(P))