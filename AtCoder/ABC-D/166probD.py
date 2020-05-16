import sys
input = sys.stdin.readline

X = int(input())


for B in range(10**3):
    for A in range(B+1, 10**14):
        t = A**5 - B**5
        if t > X:
            break
        elif t == X:
            a1, a2 = A, B
            break

for B in range(10**3):
    for A in range(10**3):
        t = A**5 + B**5
        if t > X:
            break
        elif t == X:
            a1, a2 = A, -B
            break

print(a1, a2)