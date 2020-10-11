import sys
input = sys.stdin.buffer.readline

MAX = 20

def solve(N, A, B):
    connects = set()
    for a, b in zip(A, B):
        if a > b:
            return -1
        if a < b:
            a -= ord("a")
            b -= ord("a")
            connects.add((a, b))
    
    ans = 10**15
    for bit in range(1<<(MAX-1)):
        ok = True
        last = -1
        for a, b in connects:
            if (1<<a)&bit:
                if not (1<<b)&bit:
                    if last == -1:
                        last = b
                    elif last != b:
                        ok = False
                        break
            else:
                ok = False
                break
        if ok:
            ans = min(ans, bin(bit).count("1"))
    return ans
                


Q = int(input())
for _ in range(Q):
    N = int(input())
    A = list(input().rstrip())
    B = list(input().rstrip())
    print(solve(N, A, B))
