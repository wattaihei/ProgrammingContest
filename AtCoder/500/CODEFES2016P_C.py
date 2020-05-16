import sys
input = sys.stdin.readline


N = int(input())
A = [int(input()) for _ in range(N)]

w = 0
for a in A:
    w ^= a

canuse = [True]*N

ans = 0
while w != 0:
    l = w.bit_length()-1
    use = -1
    for i, a in enumerate(A):
        if (1<<l)&a and canuse[i] and not (1<<l)&(a-1):
            canuse[i] = False
            use = a
            break
    if use == -1:
        ans = -1
        break
    ans += 1
    w = w ^ use ^ (use-1)
print(ans)