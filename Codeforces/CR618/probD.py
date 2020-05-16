import sys
input = sys.stdin.readline

N = int(input())
Points = [list(map(int, input().split())) for _ in range(N)]

def check():
    if N%2 == 1:
        return False
    k = N//2
    for i in range(k-1):
        if Points[i][0] - Points[i+1][0] != - Points[i+k][0] + Points[i+k+1][0]:
            return False
        if Points[i][1] - Points[i+1][1] != - Points[i+k][1] + Points[i+k+1][1]:
            return False
    return True

if __name__ == "__main__":
    print("YES" if check() else "NO")