A, B, K = map(int, input().split())

ans = set()
for i in range(K):
    ans.add(min(A+i, B))
    ans.add(max(B-i, A))
E = sorted(list(ans))
for e in E:
    print(e)