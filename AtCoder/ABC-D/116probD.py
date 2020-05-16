from operator import itemgetter

N, K = map(int, input().split())
TD = [list(map(int, input().split())) for _ in range(N)]

TD.sort(key=itemgetter(1), reverse=True)

remain = []
removable = []
used = [False for _ in range(N+1)]
val = 0
S = 0
for i, (t, d) in enumerate(TD):
    if i < K:
        S += d
        if not used[t]:
            val += 1
        else:
            removable.append(d)
        used[t] = True
    else:
        if not used[t]:
            remain.append(d)
            used[t] = True

S += val**2
removable.sort()

delta = 0
ans = S
for k, r in enumerate(remain):
    if k >= len(removable):
        break
    val += 1
    delta += r - removable[k] + 2*val - 1
    ans = max(ans, S+delta)
print(ans)