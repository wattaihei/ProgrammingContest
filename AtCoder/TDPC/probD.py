import math
import sys
input = sys.stdin.readline


def main():

    N, D = map(int, input().split())
    A = [0, 0, 0]
    for i, a in enumerate([2, 3, 5]):
        while D%a == 0:
            D //= a
            A[i] += 1
    a2, a3, a5 = A
    
    if D != 1:
        print(0)
    else:
        dp = [[[[0 for _ in range(a5+1)] for _ in range(a3+1)] for _ in range(a2+1)] for _ in range(N+1)]
        dp[0][0][0][0] = 1
        for i in range(N):
            for c2 in range(a2+1):
                for c3 in range(a3+1):
                    for c5 in range(a5+1):
                        now = dp[i][c2][c3][c5]/6
                        dp[i+1][c2][c3][c5] += now
                        if c2+1 >= a2:
                            dp[i+1][a2][c3][c5] += now
                        else:
                            dp[i+1][c2+1][c3][c5] += now
                        
                        if c3+1 >= a3:
                            dp[i+1][c2][a3][c5] += now
                        else:
                            dp[i+1][c2][c3+1][c5] += now
                        
                        if c2+2 >= a2:
                            dp[i+1][a2][c3][c5] += now
                        else:
                            dp[i+1][c2+2][c3][c5] += now
                    
                        if c5+1 >= a5:
                            dp[i+1][c2][c3][a5] += now
                        else:
                            dp[i+1][c2][c3][c5+1] += now
                    
                        if c2+1 >= a2 and c3+1 >= a3:
                            dp[i+1][a2][a3][c5] += now
                        elif c2+1 >= a2:
                            dp[i+1][a2][c3+1][c5] += now
                        elif c3+1 >= a3:
                            dp[i+1][c2+1][a3][c5] += now
                        else:
                            dp[i+1][c2+1][c3+1][c5] += now

        print(dp[N][a2][a3][a5])

if __name__ == "__main__":
    main()