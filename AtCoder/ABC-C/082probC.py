import collections

N = int(input())
A = list(map(int, input().split()))

B = collections.Counter(A)

ans = 0
for key, value in B.items():
    if key == value:
        continue
    if key > value:
        ans += value
    if key < value:
        ans += value - key

print(ans)