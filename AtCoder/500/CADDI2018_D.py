N = int(input())
A = [int(input()) for _ in range(N)]

ans = 'second'
for a in A:
    if a%2 != 0:
        ans = 'first'
print(ans)