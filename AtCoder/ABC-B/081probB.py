N = int(input())
A = list(map(int, input().split()))

B = []
for a in A:
    c = 0
    while a % 2 == 0:
        a //= 2
        c += 1
    B.append(c)
print(min(B))