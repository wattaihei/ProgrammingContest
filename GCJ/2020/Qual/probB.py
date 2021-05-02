import sys
input = sys.stdin.readline

Q = int(input())
Query = [input().rstrip() for _ in range(Q)]

for ind, S in enumerate(Query):
    now = 0
    ans = ""
    for s in S:
        p = int(s)
        while now < p:
            ans += "("
            now += 1
        while now > p:
            ans += ")"
            now -= 1
        ans += s
    
    while now > 0:
        ans += ")"
        now -= 1
    
    print("Case #{}:".format(ind+1), ans)