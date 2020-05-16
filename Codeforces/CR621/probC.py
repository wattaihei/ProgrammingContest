import sys
input = sys.stdin.readline

Alp = [chr(i) for i in range(97, 97+26)]

S = list(input().rstrip())

dic = {a:0 for a in Alp}
ansdic = {}
for a in Alp:
    ansdic[a] = {}
    for b in Alp:
        ansdic[a][b] = 0

for s in S:
    for a in Alp:
        ansdic[a][s] += dic[a]
    dic[s] += 1

ans = 0
for a in Alp:
    for b in Alp:
        ans = max(ans, ansdic[a][b])
    ans = max(ans, dic[a])

print(ans)