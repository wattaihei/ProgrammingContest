import sys
input = sys.stdin.readline


N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))


B = []
for a in A:
    t = a//10000
    if Z >= t:
        Z -= t
        B.append(a-t*10000)
    else:
        B.append(a)
C = []
for b in B:
    t = b//5000
    if Y >= t:
        Y -= t
        C.append(b-t*5000)
    else:
        C.append(b)

for c in C:
    
        


print("Yes" if ok else "No")