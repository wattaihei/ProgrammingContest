import bisect

N, C, K = map(int, input().split()) # 横に2個
T = [int(input()) for _ in range(N)]

T.sort()
print(T)

inf = []
for n in range(N):
    right = bisect.bisect_right(T, T[n]+K)
    inf.append([i for i in range(n, right)])

inf.sort(key=lambda s: len(s))

checked = [False for _ in range(N)]
c = 0
while inf:
    print(inf)
    print(checked)
    rem = inf.pop()
    unchecked = False
    for re in rem:
        if not checked[re]:
            checked[re] = True
            unchecked = True
    if unchecked:
        c += 1

    
print(c)