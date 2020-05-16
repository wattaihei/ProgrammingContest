import sys
input = sys.stdin.readline

def main():
    H, W, K = map(int, input().split())
    state = [list(input()) for _ in range(H)]

    blank = [0]*H
    for h in range(H):
        for w in range(W):
            if state[h][w] == "#":
                blank[h] += 1

    ans = [[] for _ in range(H)]
    color = 0
    for h in range(H):
        if blank[h] == 0: continue
        P = []
        color += 1
        c = 1
        for w in range(W):
            P.append(color)
            if state[h][w] == "#" and c < blank[h]:
                color += 1
                c += 1
        ans[h] = P

    for h in range(H):
        if blank[h] > 0: continue
        update = False
        for g in range(h, H):
            if blank[g] > 0:
                update = True
                ans[h] = ans[g]
                break
        if not update:
            for g in reversed(range(h)):
                if blank[g] > 0:
                    ans[h] = ans[g]
                    break

    for l in ans:
        print(" ".join([str(a) for a in l]))

if __name__ == "__main__":
    main()