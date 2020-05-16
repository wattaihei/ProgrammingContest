from bisect import bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] = (A[i]-1)%K

B = [0]
for a in A:
    B.append((B[-1]+a)%K)

dic = {}
for i, b in enumerate(B):
    if not b in dic.keys():
        dic[b] = [i]
    else:
        dic[b].append(i)

ans = 0
for L in dic.values():
    for i in range(len(L)):
        #print(L, i)
        j = bisect_right(L, L[i]+K-1)
        #print(j)
        ans += j-i-1
print(ans)