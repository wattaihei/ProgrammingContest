import sys
input = sys.stdin.buffer.readline

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = "No"
for i in range(N-2):
    ok = (AB[i][0] == AB[i][1] and AB[i+1][0] == AB[i+1][1] and AB[i+2][0] == AB[i+2][1])
    if ok:
        ans = "Yes"
print(ans)