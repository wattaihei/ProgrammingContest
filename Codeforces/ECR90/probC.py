import sys
input = sys.stdin.buffer.readline

Q = int(input())
Ss = [list(input().rstrip()) for _ in range(Q)]

for S in Ss:
    L = len(S)
    D = {0 : 1}
    t = 0
    for i, s in enumerate(S):
        if chr(s) == "+":
            t += 1
        else:
            t -= 1
        if t <= 0 and not t in D:
            D[t] = i+1
    ans = L-1
    #m = min(D.keys())
    for k, v in D.items():
        ans += v
    print(ans)