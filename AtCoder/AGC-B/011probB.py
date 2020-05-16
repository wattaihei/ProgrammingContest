import heapq as hp

N = int(input())
A = list(map(int, input().split()))

B = []
for a in A:
    hp.heappush(B, a)

ans = 1
for _ in range(N-1):
    ans += 1
    a1 = hp.heappop(B)
    a2 = hp.heappop(B)
    if a1*2 < a2:
        ans = 1
    hp.heappush(B, a1+a2)
print(ans)