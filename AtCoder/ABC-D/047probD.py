N, T = map(int, input().split())
A = list(map(int, input().split()))

B = []
n = A[0]
for a in A:
    B.append(a-n)
    n = min(n, a)

B.sort(reverse=True)
c = 0
for b in B:
    if b == B[0]:
        c += 1
    else:
        break
print(c)