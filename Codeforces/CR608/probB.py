import sys
input = sys.stdin.readline

N = int(input())
S = [1 if a == 'W' else 0 for a in list(input().rstrip())]
ans = []
for i in range(1,N-1):
    if S[i-1] != S[i]:
        S[i] ^= 1
        S[i+1] ^= 1
        ans.append(i+1)

if S[N-2] != S[N-1] and N%2 == 0:
    print(-1)
else:
    if S[N-2] != S[N-1]:
        for i in range(N-1):
            if i%2 == 0:
                ans.append(i+1)
    print(len(ans))
    for a in ans:
        print(a, end=" ")