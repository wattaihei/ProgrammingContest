N = int(input())
A = list(map(int, input().split()))

n = 0
c = 0
B = []
for a in A:
    if a <= n:
        c += 1
    else:
        B.append(c)
        c = 0
    n = a
B.append(c)
print(max(B))