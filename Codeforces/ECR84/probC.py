import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
Ss = [list(map(int, input().split())) for _ in range(K)]
Gs = [list(map(int, input().split())) for _ in range(K)]

if N > 1 and M > 1:
    ans = "D"*(N-1) + "R"*(M-1)
    for i in range(M):
        if i%2 == 0:
            ans += "U"*(N-1) + "L"
        else:
            ans += "D"*(N-1) + "L"
elif M > 1:
    ans = "L"*(M-1) + "R"*(M-1)
elif N > 1:
    ans = "U"*(N-1) + 'D'*(N-1)
else:
    ans = ""

print(len(ans))
print(ans)