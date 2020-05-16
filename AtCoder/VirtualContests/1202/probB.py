from collections import Counter
N = int(input())
A = Counter(list(map(int, input().split())))
M = int(input())
B = Counter(list(map(int, input().split())))

ok = True
for k, v in B.items():
    if not k in A.keys():
        ok = False
        break
    elif A[k] < v:
        ok = False
        break
print("YES" if ok else "NO")