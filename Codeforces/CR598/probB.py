from queue import Queue
import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    m = 1
    checked = [False]*(N+1)
    q1 = Queue()
    ans = []
    for a in A:
        if a == m:
            ans.append(m)
            checked[m] = True
            while q1.qsize() > 1:
                b = q1.get()
                ans.append(b)
                checked[b] = True

            while m+1 < N:
                m += 1
                if not checked[m]: break
            
            if q1.empty():
                continue

            b = q1.get()
            if b == m:
                ans.append(m)
                checked[m] = True
                while m+1 < N:
                    m += 1
                    if not checked[m]: break
            else:
                q1.put(b)

        else:
            q1.put(a)
    while q1.qsize() > 0:
        a = q1.get()
        ans.append(a)
    for a in ans:
        print(a, end=' ')
    print()