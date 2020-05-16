import math

S = int(input())

ss = int(math.sqrt(S)) + 1
if ss >= int(1E9):
    ss = int(1E9)

x1 = 1
y2 = abs(S-ss**2)
x2 = ss
y1 = ss

print(' '.join([str(a) for a in [0, 0, x1, y1, x2, y2]]))