import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    H, W = map(int, input().split())
    state = [list(input().rstrip()) for _ in range(H)]
    Query.append((H, W, state))

def main(H, W, state):
    ok = False
    for h in range(H):
        for w in range(W):
            if state[h][w] == "A":
                ok = True
                break
        if ok:
            break
    if not ok:
        return "MORTAL"
    
    ok = False
    for h in range(H):
        for w in range(W):
            if state[h][w] == "P":
                ok = True
                break
        if ok:
            break
    if not ok:
        return 0
       
    
    ok = False
    for h in range(H):
        if state[h][0] == "P":
            ok = True
            break
    if not ok:
        return 1
    
    ok = False
    for h in range(H):
        if state[h][-1] == "P":
            ok = True
            break
    if not ok:
        return 1

    ok = False
    for w in range(W):
        if state[0][w] == "P":
            ok = True
            break
    if not ok:
        return 1

    ok = False
    for w in range(W):
        if state[-1][w] == "P":
            ok = True
            break
    if not ok:
        return 1

    for h in range(H):
        ok = False
        for w in range(W):
            if state[h][w] == "P":
                ok = True
                break
        if not ok:
            return 2
    
    for w in range(W):
        ok = False
        for h in range(H):
            if state[h][w] == "P":
                ok = True
                break
        if not ok:
            return 2
    
    if state[0][0] == "A" or state[0][-1] == "A" or state[-1][0] == "A" or state[-1][-1] == "A":
        return 2
    
    for h in range(H):
        if state[h][0] == "A" or state[h][-1] == "A":
            return 3
    for w in range(W):
        if state[0][w] == "A" or state[-1][w] == "A":
            return 3

    return 4

if __name__ == "__main__":
    for H, W, state in Query:
        ans = main(H, W, state)
        print(ans)