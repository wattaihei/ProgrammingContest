R, G, B, N = map(int, input().split())

RGB = sorted([R, G, B], reverse=True)
max1 = N // RGB[0] 

count = 0
for r in range(max1+1):
    max2 = min([N-r, (N-r*RGB[0])//RGB[1]])
    for g in range(max2+1):
        if (N - (r*RGB[0] + g*RGB[1])) % RGB[2] == 0:
            count += 1
print(count)