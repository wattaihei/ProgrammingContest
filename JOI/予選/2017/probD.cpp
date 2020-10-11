#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int N, M;
vector<int> A;

int solve() {
    int S[M][N+1];
    for (int m=0; m<M; m++) {
        S[m][0] = 0;
        for (int i=0; i<N; i++) {
            S[m][i+1] = S[m][i];
            if (A[i] == m) S[m][i+1]++;
        }
    }

    vector<int> dp(1<<M, N+1);
    dp[0] = 0;
    for (int bit=0; bit<(1<<M); bit++) {
        vector<int> toConsider;
        int cnt = 0;
        for (int m=0; m<M; m++) {
            if (bit&(1<<m)) {
                cnt += S[m][N];
            } else {
                toConsider.push_back(m);
            }
        }
        for (int m : toConsider) {
            int l = S[m][N];
            dp[bit|(1<<m)] = min(dp[bit|(1<<m)], dp[bit] + l - (S[m][cnt+l] - S[m][cnt]));
        }
    }

    return dp[(1<<M)-1];
}

int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        int a; cin >> a;
        A.push_back(a-1);
    }
    cout << solve() << endl;
}