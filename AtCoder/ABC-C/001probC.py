A, B = map(int, input().split())

K = [113, 338, 563, 788, 1013, 1238, 1463, 1688, 1913, 2138, 2363, 2588, 2813, 3038, 3263, 3488]
D = ['NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']

for i in range(16):
    if i == 15:
        a1 = D[i]
        break
    if K[i] <= A < K[i+1]:
        a1 = D[i]
        break

P = [0, 0.25, 1.55, 3.35, 5.45, 7.95, 10.75, 13.85, 17.15, 20.75, 24.45, 28.45, 32.65]

for i in range(13):
    if i == 12:
        a2 = i
        break
    if P[i]*60 <= B < P[i+1]*60:
        a2 = i
        break

if a2 == 0:
    a1 = 'C'
print(a1, a2)