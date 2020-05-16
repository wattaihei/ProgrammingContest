import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

max_occupied = [False]*(N+3)
min_occupied = [False]*(N+3)
a1 = 0
a2 = 0
for a in A:
    need = True
    for n in [a-1, a, a+1]:
        if not max_occupied[n]:
            max_occupied[n] = True
            a1 += 1
            break
    for n in [a-1, a, a+1]:
        if min_occupied[n]:
            need = False
    if need:
        min_occupied[a+1] = True
        a2 += 1

print(a2, a1)
