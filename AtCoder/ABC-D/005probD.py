import sys
input = sys.stdin.readline

N = int(input())
N += 1
state = [[0]*N if i == 0 else [0] + list(map(int, input().split())) for i in range(N)]
Q = int(input())
Query = [int(input()) for _ in range(Q)]

for i in range(1, N):
    for j in range(1, N):
        state[i][j] += state[i-1][j] + state[i][j-1] - state[i-1][j-1]

dic = {}
for il in range(N-1):
    for ir in range(il+1, N):
        for jl in range(N-1):
            for jr in range(jl+1, N):
                size = (jr-jl)*(ir-il)
                s = state[ir][jr] - state[ir][jl] - state[il][jr] + state[il][jl]
                if not size in dic.keys():
                    dic[size] = s
                else:
                    dic[size] = max(dic[size], s)

for p in Query:
    ans = 0
    for size, s in dic.items():
        if p >= size:
            ans = max(ans, s)
    print(ans)