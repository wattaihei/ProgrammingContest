from collections import Counter


def main():
    N, K = map(int, input().split())
    S = list(input())

    T = sorted(S)

    change = 0
    ans = ''
    for i, s in enumerate(S):
        #print(ans)
        #print(T)
        R = Counter(S[i+1:])
        for j, t in enumerate(T):
            if t == s:
                rem = s
                break
            Q = Counter(T[:j] + T[j+1:])
            error = 0
            for k, v in Q.items():
                if not R[k]:
                    error += v
                elif v > R[k]:
                    error += v-R[k]
            #print(s, t)
            #print(R, Q, error)
            if error + change < K:
                change += 1
                rem = t
                break
        T.remove(rem)
        ans += rem

    print(''.join(ans))

if __name__ == "__main__":
    main()