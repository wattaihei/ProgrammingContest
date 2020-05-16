import sys
input = sys.stdin.readline
from collections import deque


def main():
    S = list(input().rstrip())

    P = [0]*10
    for i in range(len(S)-1):
        P[(int(S[i+1])-int(S[i]))%10] += 1

    ans = [[0]*10 for _ in range(10)]
    for x in range(10):
        for y in range(10):
            Score = [-1]*10
            Score[x] = 0
            Score[y] = 0
            q = deque()
            q.appendleft(x)
            q.appendleft(y)
            while q:
                a = q.pop()
                Ns = [(a+x)%10, (a+y)%10]
                for n in Ns:
                    if Score[n] == -1:
                        Score[n] = Score[a] + 1
                        q.appendleft(n)
            now = 0
            for num in range(10):
                if P[num] > 0 and Score[num] == -1:
                    now = -1
                    break
                now += P[num]*Score[num]
            ans[x][y] = now

    for y in range(10):
        print(*ans[y])


if __name__ == "__main__":
    main()