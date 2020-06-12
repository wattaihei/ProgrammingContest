import sys
input = sys.stdin.readline

N = int(input())
state = [list(input().rstrip()) for _ in range(N)]

P = ""
for i in range(N//2):
    tmp = ""
    for s in state[i]:
        for t in state[N-1-i]:
            if s == t:
                tmp = s
                break
        if tmp:
            break
    if tmp:
        P += tmp
    else:
        P = ""
        break

if not P and N != 1:
    print(-1)
else:
    if N%2 == 0:
        ans = P + P[::-1]
    else:
        ans = P + state[N//2][0] + P[::-1]
    print(ans)