import sys
input = sys.stdin.readline

N, C = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 10**15
for c1 in range(1, 11):
    for c2 in range(1, 11):
        if c1 == c2: continue
        score = 0
        for i, a in enumerate(A):
            if i%2 == 0 and a != c1:
                score += C
            elif i%2 == 1 and a != c2:
                score += C
        ans = min(ans, score)
print(ans)