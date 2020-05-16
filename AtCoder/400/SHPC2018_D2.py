import sys
input = sys.stdin.readline

from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
import numpy as np

N, M, S, G = map(int, input().split())
ABCD = np.array([list(map(int, input().split())) for _ in range(M)])
A = ABCD[:, 0]
B = ABCD[:, 1]
C = ABCD[:, 2]
D = ABCD[:, 3]

graph_y = csr_matrix((C, (A, B)), (N+1, N+1))
graph_s = csr_matrix((D, (A, B)), (N+1, N+1))

Ds = dijkstra(graph_y, directed=False, indices=S).astype('int64')
Dg = dijkstra(graph_s, directed=False, indices=G).astype('int64')

ans = Ds + Dg
for i in reversed(range(1, N)):
    ans[i] = min(ans[i+1], ans[i])

for n in range(1, N+1):
    print(10**15-ans[n])