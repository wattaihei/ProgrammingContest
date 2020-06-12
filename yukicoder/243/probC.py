import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    ans = N + N**2-1 + (N-1)**2
    dic = {}
    for n in range(2, N+1):
        if 2**n > N: break
        for p in range(2, N+1):
            m = p**n
            if m > N: break
            if m in dic:
                dic[m] += 1
            else:
                dic[m] = 1
    for c in dic.values():
        ans += (c+1)*c
    print(ans)