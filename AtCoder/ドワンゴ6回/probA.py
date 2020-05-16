import sys
input = sys.stdin.readline

N = int(input())
P = [list(map(str, input().split())) for _ in range(N)]
S = input().rstrip()

ind = -1
for a, b in P:
    if a == S:
        ind = 0
    elif ind != -1:
        ind += int(b)

print(ind)