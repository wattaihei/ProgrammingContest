import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

ans = 0
dic = {}
for a in A:
    if not a in dic:
        dic[a] = 1
    else:
        dic[a] += 1
    ans += a


for b, c in Query:
    if b in dic:
        count = dic[b]
        if c in dic:
            dic[c] += count
        else:
            dic[c] = count
        del dic[b]
        ans += (c-b)*count
    print(ans)
    
