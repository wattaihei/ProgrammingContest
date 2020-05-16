import sys
input = sys.stdin.readline

N = int(input())
Arrays = [list(map(int, input().split())) for _ in range(N-2)]

dic = {}
for A in Arrays:
    A.sort()
    for a in A:
        if a in dic:
            dic[a].append(A)
        else:
            dic[a] = [A]

for n in range(1, N+1):
    if len(dic[n]) == 1:
        start = n
        break

for m in dic[n][0]:
    if len(dic[m]) == 2:
        second = m
    elif len(dic[m]) == 3:
        third = m

ans = [start, second, third]
num = third
for _ in range(N-3):
    now = set(ans[-3:])
    for A in dic[num]:
        T = []
        for a in A:
            if not a in now:
                T.append(a)
        if len(T) == 1:
            next_num = T[0]
            break
    ans.append(next_num)
    num = next_num

print(*ans)