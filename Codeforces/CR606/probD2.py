import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    Ss = [input().rstrip() for _ in range(N)]
    Query.append((N, Ss))

for N, Ss in Query:
    dic = {}
    A = [set() for _ in range(4)]
    Pair = 0
    for i, S in enumerate(Ss):
        if S[0] == '1' and S[-1] == "1":
            A[3].add(i)
        elif S[0] == '1' and S[-1] == "0":
            T = S[::-1]
            if T in dic.keys():
                Pair += 1
                A[1].remove(dic[T])
            else:
                dic[S] = i
                A[2].add(i)
        elif S[0] == '0' and S[-1] == "1":
            T = S[::-1]
            if T in dic.keys():
                Pair += 1
                A[2].remove(dic[T])
            else:
                dic[S] = i
                A[1].add(i)
        else:
            A[0].add(i)
    x1 = Pair + len(A[1])
    x2 = Pair + len(A[2])
    if x1 == x2 or x1 == x2 + 1 or x1 == x2 - 1:
        if x1 == 0 and x2 == 0 and (len(A[0]) > 0 and len(A[3]) > 0):
            print(-1)
        else:
            print(0)
            print()
    elif x1 > x2:
        must = (x1 - x2) // 2
        print(must)
        ans = []
        for a in A[1]:
            ans.append(a)
            if len(ans) == must:
                break
        print(" ".join([str(a+1) for a in ans]))
    elif x2 > x1:
        must = (x2 - x1) // 2
        print(must)
        ans = []
        for a in A[2]:
            ans.append(a)
            if len(ans) == must:
                break
        print(" ".join([str(a+1) for a in ans]))             