import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left

def solve(N, M, AB):
    As = []
    for a, _ in AB:
        As.append(a)
    
    As.sort()
    sA = [0]
    for a in As:
        sA.append(a+sA[-1])
    
    ans = sA[-1] - sA[-1-min(M,N)]
    
    for a, b in AB:
        ind = bisect_left(As, b)
        countA = M - ind
        if a >= b:
            countA = min(countA, N)
            score = sA[-1] - sA[-1-countA] + (N-countA)*b
        else:
            countA = min(countA, N-1)
            score = a + sA[-1] - sA[-1-countA] + (N-countA-1)*b
        ans = max(ans, score)
    return ans
        

Q = int(input())
for q in range(Q):
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    if q != Q-1:
        input()
    print(solve(N, M, AB))