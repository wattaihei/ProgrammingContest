N = int(input())
A = list(map(int, input().split()))

m = 0
B = []
for a in A:
    if a < 0:
        m += 1
    B.append(abs(a))

if m % 2 == 0:
    print(sum(B))
else:
    print(sum(B)-2*min(B))