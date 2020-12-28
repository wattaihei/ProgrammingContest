import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

tmp_c = 0
ans = 1
for n in range(2, 1001):
    c = 0
    for a in A:
        if a%n == 0:
            c += 1
    if c > tmp_c:
        tmp_c = c
        ans = n

print(ans)