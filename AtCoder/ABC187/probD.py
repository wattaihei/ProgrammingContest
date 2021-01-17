import sys
input = sys.stdin.buffer.readline

N = int(input())
AB = [list(map(int, input().rstrip().split())) for _ in range(N)]

Aoki = 0
Tak = []
for b, a in AB:
    Aoki += b
    Tak.append(a+2*b)

Tak.sort(reverse=True)

ans = 0
while Aoki >= 0:
    Aoki -= Tak[ans]
    ans += 1

print(ans)