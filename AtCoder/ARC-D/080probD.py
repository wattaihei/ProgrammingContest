H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

B = []
for i, a in enumerate(A):
    B.extend([i+1]*a)

h = -1
ans = []
for i, b in enumerate(B):
    if i % W == 0:
        h += 1
        C = []
    C.append(b)
    if i % W == W-1:
        if h%2 == 0:
            ans.append(C)
        else:
            ans.append(C[::-1])

for C in ans:
    print(' '.join([str(c) for c in C]))
