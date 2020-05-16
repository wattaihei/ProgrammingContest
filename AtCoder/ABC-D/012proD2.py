import numpy as np
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from scipy.sparse import csr_matrix

N, M = map(int, input().split())
ABT = np.array([list(map(int, input().split())) for _ in range(M)])

A = ABT[:, 0]
B = ABT[:, 1]
T = ABT[:, 2]

graph = csr_matrix((T, (A, B)), (N+1, N+1))

dist = floyd_warshall(graph, directed=False)
ans = dist[1:, 1:].max(axis=1).min().astype(int)
print(ans)