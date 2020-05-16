import sys
input = sys.stdin.readline

L, R, M, K = map(int, input().split())

a1 = K*L//M
a2 = K*R//M
print("Yes" if K*L%M == 0 or a1 != a2 else "No")