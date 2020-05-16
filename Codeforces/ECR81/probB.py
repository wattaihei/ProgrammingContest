import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, X = map(int, input().split())
    A = input().rstrip()
    Query.append((N, X, A))

for N, X, A in Query:
    tmp = 0
    Max = 0
    Min = 0
    T = [0]
    for a in A:
        if int(a):
            tmp -= 1
        else:
            tmp += 1
        T.append(tmp)
        Max = max(Max, tmp)
        Min = min(Min, tmp)
    
    cycle = T.pop()
    if cycle == 0:
        ans = 0
        for t in T:
            if t == X:
                ans = -1
                break
    else:
        ans = 0
        for t in T:
            if (t-X)%cycle == 0 and (t-X)//cycle <= 0:
                ans += 1
    print(ans)
