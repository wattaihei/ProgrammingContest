import sys
input = sys.stdin.readline

X = int(input())
A = [i-1 for i in range(X+1)]
for x in range(2, X+1):
    p = x
    while p <= X:
        A[p] -= 1
        p += x

ans = []
s = 10**13
for x in range(1, X):
    y = X-x
    score = abs(A[x]-A[y])
    if score < s:
        ans = [(x, y)]
        s = score
    elif score == s:
        ans.append((x, y))

# if X%2 == 0:
#     x = X//2
#     if s != 0:
#         ans = [(x, x)]
#     elif s == 0:
#         ans.append((x, x))


print("\n".join([str(a)+" "+str(b) for a, b in ans]))
