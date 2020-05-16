import math
import sys
input = sys.stdin.readline

Q = int(input())
AB = [list(map(int, input().split())) for _ in range(Q)]

for A, B in AB:
    P = A*B-1
    b = int(math.sqrt(P))
    if b <= 1:
        if P <= 1:
            print(0)
        else:
            print(1)
        continue
    K = []
    for n in [b-1, b, b+1]:
        if P//n > n:
            border = n
        K.append(min(n, P//n))
    ans = 2*border
    if P//(border+1) == border+1:
        ans += 1
    if min(A, B) <= max(K):
        ans -= 1

    print(ans)