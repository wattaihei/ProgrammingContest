import sys
input = sys.stdin.readline

N, W = map(int, input().split())
A = [[] for _ in range(4)]
for i in range(N):
    w, v = map(int, input().split())
    if i == 0: w0 = w
    A[w-w0].append(v)

B = [[0] for _ in range(4)]
for i in range(4):
    A[i].sort(reverse=True)
    b = 0
    for a in A[i]:
        b += a
        B[i].append(b)
#print(B)
ans = 0
for n1, b1 in enumerate(B[0]):
    for n2, b2 in enumerate(B[1]):
        for n3, b3 in enumerate(B[2]):
            n4 = min((W - n1*w0 - n2*(w0+1) - n3*(w0+2)) // (w0+3), len(B[3])-1)
            if n4 < 0: continue
            ans = max(ans, b1+b2+b3+B[3][n4])

print(ans)