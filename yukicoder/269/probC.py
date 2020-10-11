import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dic = {}
for a, b in zip(A, B):
    if a in dic:
        dic[a] += b
    else:
        dic[a] = b

AB = list(dic.items())
AB.sort()

bsum = sum(B) - 2*AB[0][1]
score = 0
pa = AB[0][0]
for a, b in AB:
    score += abs(pa-a) * b

a0, a1 = score, pa
for a, b in AB[1:]:
    score -= (a-pa)*bsum
    if a0 > score:
        a0, a1 = score, a
    bsum -= 2*b
    pa = a

print(a1, a0)