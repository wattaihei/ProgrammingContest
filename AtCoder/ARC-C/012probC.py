import sys
input = sys.stdin.readline

state = [list(input().rstrip()) for _ in range(19)]

def finished(m):
    for h in range(19):
        seq = 0
        for w in range(19):
            if state[h][w] == m:
                seq += 1
            else:
                seq = 0
            if seq == 5:
                return False
    for w in range(19):
        seq = 0
        for h in range(19):
            if state[h][w] == m:
                seq += 1
            else:
                seq = 0
            if seq == 5:
                return False
    for k in range(-19, 19):
        seq = 0
        for h in range(max(0, k), min(19, 19+k)):
            if state[h][h-k] == m:
                seq += 1
            else:
                seq = 0
            if seq == 5:
                return False
    for k in range(-19, 19):
        seq = 0
        for h in range(max(0, k), min(19, 19+k)):
            if state[h-k][18-h] == m:
                seq += 1
            else:
                seq = 0
            if seq == 5:
                return False
    return True

def main():
    white = 0
    black = 0
    for h in range(19):
        for w in range(19):
            if state[h][w] == "o":
                white += 1
            if state[h][w] == "x":
                black += 1
    if white != black+1 and white != black:
        return False
    whitefinished = not finished("o")
    blackfinished = not finished("x")
    if whitefinished:
        if blackfinished:
            return False
        if white == black:
            return False
    if blackfinished:
        if white == black+1:
            return False
    return True

if __name__ == "__main__":
    print("YES" if main() else "NO")