import sys
input = sys.stdin.readline

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))


for N, A in Query:
    ans = []
    Nums = {}
    for a in A:
        for i, p in enumerate(primes):
            if a%p == 0:
                if not p in Nums:
                    Nums[p] = len(Nums)+1
                ans.append(Nums[p])
                break
    print(len(Nums))
    print(*ans)