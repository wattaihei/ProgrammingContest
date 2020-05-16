import sys
input = sys.stdin.readline

from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
import numpy as np

# A, B: 頂点ペア
# T : 頂点間の長さ

def main():
    N, M = map(int, input().split())
    ABT = np.array([list(map(int, input().split())) for _ in range(M)])
    K = int(input())
    XYZ = [list(map(int, input().split())) for _ in range(K)]

    A = ABT[:, 0]
    B = ABT[:, 1]
    T = ABT[:, 2]

    graph = csr_matrix((T, (A, B)), (N+1, N+1))
    dist = floyd_warshall(graph, directed=False)[1:, 1:].astype(np.int64)

    for x, y, z in XYZ:
        np.minimum(dist, dist[x-1][:, None]+dist[y-1][None, :]+z, out=dist)
        np.minimum(dist, dist.T, out=dist)
        s = dist.sum()//2
        print(s)
    

if __name__ == "__main__":
    main()