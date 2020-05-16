import sys
input = sys.stdin.readline

dic = {"R": [], "G": [], "B": []}

N = int(input())
S = list(input().rstrip())

for i, s in enumerate(S):
    dic[s].append(i)

Bs = set(dic["B"])

ans = 0
for nr in dic["R"]:
    for ng in dic["G"]:
        if nr < ng:
            d = ng - nr
            nos = [nr - d, ng + d]
        else:
            d = nr - ng
            nos = [ng - d, nr + d]
        
        if (nr-ng)%2 == 0:
            nos.append((nr+ng)//2)
        
        ans += len(Bs)
        for no in nos:
            if no in Bs:
                ans -= 1

print(ans)