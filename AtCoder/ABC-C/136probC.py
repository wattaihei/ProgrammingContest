import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

H = H[::-1]
ans = 'Yes'
for i in range(N-1):
    #print(i, H[i], H[i+1])
    if H[i] < H[i+1]:
        if H[i] == H[i+1] - 1:
            H[i+1] -= 1
            continue
        else:
            ans = 'No'

print(ans)