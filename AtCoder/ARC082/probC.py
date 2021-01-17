import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

dic = {}
for a in A:
    dic[a] = dic.get(a, 0) + 1

ans = 0
for a, c in dic.items():
    s = c + dic.get(a+1, 0) + dic.get(a-1, 0)
    ans = max(ans, s)

print(ans)