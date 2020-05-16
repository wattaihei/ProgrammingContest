import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dic = {}
for i,a in enumerate(A):
    b = a-i
    if b in dic:
        dic[b] += a
    else:
        dic[b] = a

print(max(list(dic.values())))