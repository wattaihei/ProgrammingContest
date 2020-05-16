N = int(input())
S = input()

dp = [0]*N
j = 1

for i in range(N):
    while S[i:j] in S[j:N]:
        dp[i] = j-i
        j += 1
print(max(dp))