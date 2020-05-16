import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip())
    S = input()
    Q = int(input())
    Ks = list(map(int, input().split()))

    for K in Ks:
        # [D, M, DM, DMC]
        dp = [0]*4
        for i in range(N):
            if i-K >= 0:
                sk = S[i-K]
                if sk == 'D':
                    dp[0] -= 1
                    dp[2] -= dp[1]
                elif sk == "M":
                    dp[1] -= 1
            s = S[i]
            if s == "D":
                dp[0] += 1
            elif s == 'M':
                dp[1] += 1
                dp[2] += dp[0]
            elif s == 'C':
                dp[3] += dp[2]
        
        print(dp[3])
    

if __name__ == "__main__":
    main()