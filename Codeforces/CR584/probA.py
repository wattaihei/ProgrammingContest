import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

used = []
A.sort()
for a in A:
    must = True
    for u in used:
        if a%u == 0:
            must = False
            break
    if must:
        used.append(a)

print(len(used))