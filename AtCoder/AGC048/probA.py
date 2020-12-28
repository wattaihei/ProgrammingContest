import sys
input = sys.stdin.readline

atcoder = list("atcoder")

def solve(T):

    ans = 10**18
    tmp = 0
    used = [False]*len(T)
    for j, at in enumerate(atcoder):
        
        for i, t in enumerate(T):
            if t > at:
                ans = min(ans, )

    return ans

Q = int(input())
for _ in range(Q):
    T = list(input().rstrip())
    print(solve(T))