import sys
input = sys.stdin.readline

N = int(input())

Alp = [chr(i) for i in range(97, 97+26)]

P = 26
t = 1
L = 1
while t + P <= N:
    t += P
    L += 1
    P *= 26

seq = N - t
ans = []
for l in range(L):
    ans.append(Alp[seq % 26])
    seq //= 26

print("".join(ans[::-1]))