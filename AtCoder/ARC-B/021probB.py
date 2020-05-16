import sys
input = sys.stdin.readline

L = int(input())
B = [int(input()) for _ in range(L)]

a = 0
ans = [0]
for b in B:
    a = a ^ b
    ans.append(a)
last = ans.pop()
if last != 0:
    print(-1)
else:
    for a in ans:
        print(a)