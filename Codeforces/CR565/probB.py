import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    count = [0, 0, 0]
    for a in A:
        count[a%3] += 1
    a1, a2 = count[1], count[2]
    ans = count[0]
    if a1 >= a2:
        ans += a2 + (a1-a2)//3
    else:
        ans += a1 + (a2-a1)//3
    print(ans)