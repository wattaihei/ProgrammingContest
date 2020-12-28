import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

D = [[], []]
ans = 0
for i, (a, b) in enumerate(zip(A, B)):
    ans += a
    D[i%2].append(b-a)

D[0].sort(reverse=True)
D[1].sort(reverse=True)

for d1, d2 in zip(D[0], D[1]):
    ans += max(d1+d2, 0)

print(ans)