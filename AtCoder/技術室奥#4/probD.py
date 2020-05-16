N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

if (P+Q)%2 != 0:
    ans = 0
else:
    ax = (P+Q)//2
    ayz = (P-Q)//2

    Az = {}
    for a in A:
        Az[a] = 0
        Az[ayz-a] = 0
    
    ans = 0
    cx = 0
    for i, a in enumerate(A):
        if a == ax:
            cx += 1
        ans += Az[ayz - a]
        Az[a] += cx
print(ans)
