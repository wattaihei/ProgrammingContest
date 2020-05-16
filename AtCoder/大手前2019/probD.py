N, M = map(int, input().split())
S = [input() for _ in range(M)]

mod = int(1E9+7)

def main():

    dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(M+1)]
    #dp[0][0][0] = 0
    dp[0][0][1] = 3
    dp[0][0][2] = 2
    if M == 0:
        for i in range(1, N):
            #dp[0][i][0] = 0
            dp[0][i][1] = (3*dp[0][i-1][1] + 2*dp[0][i-1][2]) % mod
            dp[0][i][2] = (3*dp[0][i-1][1] + 3*dp[0][i-1][2]) % mod
        return sum(dp[0][-1]) % mod
    
    if S[0] == 'Fizz':
        dp[1][0][0] = 3
        #dp[1][0][1] = 0
        #dp[1][0][2] = 0
    elif S[0] == 'Buzz':
        #dp[1][0][0] = 0
        #dp[1][0][1] = 0
        dp[1][0][2] = 1
    #elif S[0] == 'FizzBuzz':
    #    dp[1][0][0] = 0
    #    dp[1][0][1] = 0
    #    dp[1][0][2] = 0

    for i in range(1, N):
        #dp[0][i][0] = 0
        dp[0][i][1] = (3*dp[0][i-1][1] + 2*dp[0][i-1][2]) % mod
        dp[0][i][2] = (3*dp[0][i-1][1] + 3*dp[0][i-1][2]) % mod
        for j in range(1, M+1):
            if S[j-1] == 'Fizz':
                dp[j][i][0] = (3*dp[j-1][i-1][0] + 2*dp[j-1][i-1][1] + 3*dp[j-1][i-1][2]) % mod
                #dp[j][i][1] = 0
                #dp[j][i][2] = 0
            elif S[j-1] == 'Buzz':
                #dp[j][i][0] = 0
                dp[j][i][1] = (dp[j-1][i-1][1] + dp[j-1][i-1][2]) % mod
                dp[j][i][2] = (dp[j-1][i-1][0] + dp[j-1][i-1][2]) % mod
            else:
                dp[j][i][0] = (dp[j-1][i-1][0] + dp[j-1][i-1][1]) % mod
                #dp[j][i][1] = 0
                #dp[j][i][2] = 0

            #dp[j][i][0] += 0
            dp[j][i][1] += (3*dp[j][i-1][0] + 3*dp[j][i-1][1] + 2*dp[j][i-1][2]) % mod
            dp[j][i][2] += (2*dp[j][i-1][0] + 3*dp[j][i-1][1] + 3*dp[j][i-1][2]) % mod

    return sum(dp[-1][-1])%mod


if __name__ == "__main__":
    print(main())