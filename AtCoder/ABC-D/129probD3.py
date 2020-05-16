import copy
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
S = [[1 if a == '.' else 0 for a in list(input())]  for _ in range(H)]

def main():
    R = copy.deepcopy(S)
    for h in range(H):
        s = 0
        for w in range(W):
            if R[h][w] == 1:
                s += 1
                R[h][w] = s
            else:
                s = 0
        l = 0
        for w in range(W-1, -1, -1):
            if R[h][w] > 0:
                l = max(l, R[h][w])
                R[h][w] = l
            else:
                l = 0

    L = copy.deepcopy(S)
    for w in range(W):
        s = 0
        for h in range(H):
            if L[h][w] == 1:
                s += 1
                L[h][w] = s
            else:
                s = 0
        l = 0
        for h in range(H-1, -1, -1):
            if L[h][w] > 0:
                l = max(l, L[h][w])
                L[h][w] = l
            else:
                l = 0
    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans, L[h][w]+R[h][w]-1)
    print(ans)

if __name__ == "__main__":
    main()