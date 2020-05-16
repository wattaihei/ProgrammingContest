N, K = map(int, input().split()) # 横に2個
L = [list(map(int, input().split())) for _ in range(N-1)]

mod = 10**9+7

neardic = {}
checked = {}
for p in range(1, N+1):
    near = []
    for l in L:
        if p in l:
            other = set(l) - {p}
            near.append(list(other)[0])
    neardic[p] = set(near)
    checked[p] = False


def color(p=1, state=[1], prob=K, checked=checked):
    checked[p] = True
    nears = neardic[p]
    leaf = True
    for near in nears:
        if not checked[near]:
            leaf = False
            break
    if leaf:
        state.pop()
        return prob
    
    nextprobmax = K-1 if len(state) == 1 else K-2
    c = 0
    for i, near in enumerate(nears):
        if checked[near]:
            c += 1
            continue
        prob = prob * (nextprobmax - i + c) % mod
        state.append(near)
        prob = color(near, state, prob, checked)
    return prob

print(color())