import sys
input = sys.stdin.readline

N = int(input())

ans = []
if N%2 == 0:
    MAX = N*2 + 3
    for k in range(MAX):
        ans.append((0, k))
    ans += [(1, 0), (1, MAX-1), (2, 0), (2, MAX-1), (3, 0), (3, MAX-1), (4, 0), (4, MAX-1), (4, 1), (4, MAX-2)]
    for k in range(2, MAX-2):
        ans.append((4, k))
        if k%4 != 1:
            ans.append((2, k))
            ans.append((6, k))
        if k%2 == 0:
            ans.append((3, k))
            ans.append((5, k))
else:
    MAX = N*2 + 3
    for k in range(MAX):
        ans.append((0, k))
        ans.append((8, k))
    ans += [(1, 0), (1, MAX-1), (7, 0), (7, MAX-1)]
    for k in range(MAX):
        ans.append((4, k))
        if k%4 != 1:
            ans.append((2, k))
        if k%4 != 3:
            ans.append((6, k))
        if k%2 == 0:
            if k != MAX-1:
                ans.append((3, k))
            if k != 0:
                ans.append((5, k))

print(len(ans))
for a, b in ans:
    print(a, b)

# G = [0]*11
# for a, b in ans:
#     G[a] |= (1<<b)

# for g in G:
#     q = "0"*(30-len(bin(g))) + bin(g)[2:]
#     print(q)