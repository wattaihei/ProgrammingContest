import sys
input = sys.stdin.readline

N = int(input())

grundy = 0
for _ in range(N):
    X, Y, Z = map(int, input().split())
    M = int(input())
    maxX = -1
    minX = X+1
    maxY = -1
    minY = Y+1
    maxZ = -1
    minZ = Z+1
    for _ in range(M):
        x, y, z = map(int, input().split())
        maxX = max(x, maxX)
        minX = min(x, minX)
        maxY = max(y, maxY)
        minY = min(y, minY)
        maxZ = max(z, maxZ)
        minZ = min(z, minZ)
    grundy ^= (X-maxX-1) ^ minX ^ (Y-maxY-1) ^ minY ^ (Z-maxZ-1) ^ minZ

print("WIN" if grundy else "LOSE")