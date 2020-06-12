import sys
input = sys.stdin.readline
import math

A, B, H, M = map(int, input().split())

theta_min = 2*math.pi/60*M
theta_hour = 2*math.pi/(60*12)*(H*60+M)

x1, y1 = A*math.cos(theta_hour), A*math.sin(theta_hour)
x2, y2 = B*math.cos(theta_min), B*math.sin(theta_min)
print(math.sqrt((x1-x2)**2+(y1-y2)**2))