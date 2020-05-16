from collections import Counter

N = int(input())
A = list(map(int, input().split()))

B = []
for a in A:
    while a % 2 == 0:
        a = a // 2
    B.append(a)

c = len(Counter(B))
print(c)