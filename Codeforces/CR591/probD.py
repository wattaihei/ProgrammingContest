import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    dic = {}
    for i, a in enumerate(A):
        if not a in dic:
            dic[a] = [i]
        else:
            dic[a].append(i)
    Nums = sorted(list(dic.keys()))
    L = len(Nums)
    ans = L + 1
    ind = 0
    for i in range(L):
        if ind <= i:
            last = -1
        while ind < L:
            n = Nums[ind]
            if last < dic[n][0]:
                last = dic[n][-1]
                ind += 1
            else:
                break
        ans = min(i + max(L-ind, 0), ans)
    print(ans)
