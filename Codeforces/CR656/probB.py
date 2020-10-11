import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    t = set()
    ans = []
    for a in A:
        if not a in t:
            ans.append(a)
        t.add(a)
    print(*ans)