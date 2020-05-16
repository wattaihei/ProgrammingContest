from operator import itemgetter

N, M = map(int, input().split())
dic = {}
A = list(map(int, input().split()))
for a in A:
    if not a in dic.keys():
        dic[a] = 1
    else:
        dic[a] += 1

for _ in range(M):
    b, c = map(int, input().split())
    if not c in dic.keys():
        dic[c] = b
    else:
        dic[c] += b
    
#print(dic)
L = list(dic.items())
L.sort(reverse=True, key=itemgetter(0))

c = 0
ans = 0
for k, v in L:
    if c + v >= N:
        ans += (N-c)*k
        break
    ans += k*v
    c += v
print(ans)