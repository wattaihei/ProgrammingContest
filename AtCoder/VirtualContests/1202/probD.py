import sys
input = sys.stdin.readline

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

D = []
for a in A:
    for b in B:
        D.append(a+b)
D.sort(reverse=True)

E = []
for i in range(min(K, len(D))):
    for c in C:
        E.append(D[i]+c)

E.sort(reverse=True)
for i in range(K):
    print(E[i])