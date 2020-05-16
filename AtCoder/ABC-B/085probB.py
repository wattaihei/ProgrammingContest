from collections import Counter

N = int(input())
D = [int(input()) for _ in range(N)]

a = len(Counter(D))
print(a)