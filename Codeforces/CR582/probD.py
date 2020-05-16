import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

dic = {}
for a in A:
    count = 0
    while a:
        if a in dic:
            dic[a].append(count)
        else:
            dic[a] = [count]
        count += 1
        a //= 2

ans = 10**14
for k, L in dic.items():
    if len(L) < K:
        continue
    L.sort()
    p = sum(L[:K])
    if p < ans:
        ans = p
print(ans)