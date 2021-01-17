import sys
input = sys.stdin.buffer.readline

N = int(input())
P = list(map(lambda x:int(x)-1, input().rstrip().split()))

ans = 0
for i in range(N-1):
    if P[i] == i:
        j = P[i+1]
        P[i+1] = i
        P[i] = j
        ans += 1

if P[N-1] == N-1:
    ans += 1

print(ans)