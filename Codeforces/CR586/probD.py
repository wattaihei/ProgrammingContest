import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dic = {}
for a in A:
    c = (a&-a).bit_length()
    if c in dic:
        dic[c].append(a)
    else:
        dic[c] = [a]

L = []
num = -1
for k, lst in dic.items():
    if len(lst) > len(L):
        L = lst
        num = k

ans = []
for k, lst in dic.items():
    if k != num:
        ans += lst

print(len(ans))
print(*ans)