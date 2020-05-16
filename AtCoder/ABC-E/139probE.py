import heapq as hp
from bisect import bisect_left, bisect_right

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

state = []
for i in range(N):
    Ai = [i+1, A[i][0]]
    state.append(sorted(Ai))

ind = [0 for _ in range(N)]
for i, a, b in enumerate(state):
    if a == pa and b == pb:


while True:
    P = [p+1, A[p][ind[p]]]
    P.sort()
    hp.heappush(state, P)
    