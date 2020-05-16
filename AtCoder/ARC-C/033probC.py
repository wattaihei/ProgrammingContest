import sys
input = sys.stdin.readline

Q = int(input())
TX = [list(map(int, input().split())) for _ in range(Q)]

max_X = 0
for _, X in TX:
    max_X = max(max_X, X)

# binary indexed tree
bit = [0 for _ in range(max_X+1)]

# 0からiまでの区間和
# 立っているビットを下から処理
def query_sum(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

# i番目の要素にxを足す
# 覆ってる区間すべてに足す
def add(i, x):
    while i <= max_X:
        bit[i] += x
        i += i & -i

def main():
    for T, X in TX:
        if T == 1:
            add(X, 1)
        else:
            l = 0
            r = max_X
            m = max_X//2
            while l < r:
                m = (l+r)//2
                nx = query_sum(m)
                if nx >= X:
                    r = m
                else:
                    if l == m:
                        break
                    l = m
            print(r)
            add(r, -1)

if __name__ == "__main__":
    main()