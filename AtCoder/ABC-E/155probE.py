import sys
input = sys.stdin.readline

Num_str = list(input().rstrip())
L = len(Num_str)
Num = []

for n in reversed(Num_str):
    Num.append(int(n))

S = 0
up = False
for i, n in enumerate(Num):
    if up:
        n += 1
    if n < 5:
        S += n
        up = False
    elif n == 5:
        S += 5
        up = (i != L-1 and Num[i+1] >= 5)
    else:
        S += 10 - n
        up = True
if up:
    S += 1
print(S)