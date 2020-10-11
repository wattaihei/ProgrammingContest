#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int MAXN = 2e3, INF = 2e9+10;
int N;
int A[MAXN], B[MAXN];

int solve() {
    int M = 2*N+2;
    vector<int> dp(M, -INF);
    dp[N] = 0;
    for (int i=0; i<N; i++) {
        int a = A[i]-1, b = B[i];
        vector<int> ndp = dp;
        for (int m=0; m<M; m++){
            int l = min(M-1, max(0, m+a));
            ndp[l] = max(ndp[l], dp[m]+b);
        }
        dp = ndp;
    }
    int ans = -INF;
    for (int m=N-1; m<M; m++) {
        ans = max(ans, dp[m]);
    }
    return ans;
}

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> A[i] >> B[i];
    }
    cout << solve() << endl;
}