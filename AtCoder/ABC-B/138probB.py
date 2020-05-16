N = int(input())
A = list(map(int, input().split()))

B = 1
for a in A:
    B *= a
C = 0
for a in A:
    C += (B//a)
print(B/C)