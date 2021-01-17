import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

m = max(A)
m2 = -1
for a in A:
    m2 = max(m2, min(a, m-a))

m2 = m2 if m2 in A else m-m2

print(m, m2)