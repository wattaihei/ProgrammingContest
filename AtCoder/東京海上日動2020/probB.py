A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

D = abs(A-B)
if W >= V or D > (V-W)*T:
    print("NO")
else:
    print("YES")