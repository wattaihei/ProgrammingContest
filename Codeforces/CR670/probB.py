import sys
input = sys.stdin.buffer.readline

INF = 10**19

Q = int(input())
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Minus = []
    Plus = []
    for a in A:
        if a > 0:
            Plus.append(a)
        elif a < 0:
            Minus.append(-a)
        
    Plus.sort(reverse=True)
    Minus.sort(reverse=True)

    ans = -INF
    if len(Minus) >= 5:
        ans = max(ans, -Minus[-1]*Minus[-2]*Minus[-3]*Minus[-4]*Minus[-5])
    if len(Minus) >= 3 and len(Plus) >= 2:
        ans = max(ans, -Minus[-1]*Minus[-2]*Minus[-3]*Plus[-1]*Plus[-2])
    if len(Minus) >= 1 and len(Plus) >= 4:
        ans = max(ans, -Minus[-1]*Plus[-1]*Plus[-2]*Plus[-3]*Plus[-4])
    if len(Plus) >= 5:
        ans = max(ans, Plus[0]*Plus[1]*Plus[2]*Plus[3]*Plus[4])
    if len(Plus) >= 3 and len(Minus) >= 2:
        ans = max(ans, Plus[0]*Plus[1]*Plus[2]*Minus[0]*Minus[1])
    if len(Plus) >= 1 and len(Minus) >= 4:
        ans = max(ans, Plus[0]*Minus[0]*Minus[1]*Minus[2]*Minus[3])
    if 0 in A:
        ans = max(ans, 0)
    print(ans) 