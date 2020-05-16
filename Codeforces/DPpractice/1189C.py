N = int(input())
S = list(map(int, input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

for l in LR:
    q = S[l[0]-1:l[1]]
    candy = 0
    while len(q) > 1:
        qq = []
        n = len(q)
        for i in range(n//2):
            next = q[2*i] + q[2*i+1]
            if next > 9:
                candy += 1
            qq.append(next % 10)
        q = qq
    print(candy)
