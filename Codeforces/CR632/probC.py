import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

tmp = 0
dic = {0 : 1}
ans = 0
least = 0
for i, a in enumerate(A):
    tmp += a
    if a == 0:
        least = i+1
        continue
    elif tmp in dic:
        least = max(least, dic[tmp])

    ans += i+1 - least 

    dic[tmp] = i+2

print(ans)