import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

tmp = 0
for a in A:
    if a == tmp+1:
        tmp += 1
if tmp == 0:
    print(-1)
else:
    print(N-tmp)