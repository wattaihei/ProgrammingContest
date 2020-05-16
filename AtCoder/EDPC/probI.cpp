#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
    int N; cin >> N;
    double p[N];
    REP(i, N) cin >> p[i];
    double dp[N+1][N+1];
    REP(i, N+1) REP(j, N+1) dp[i][j] = 0;
    dp[0][0] = 1;
    REP(i, N){
        REP(j, N){
            dp[i+1][j+1] += dp[i][j]*p[i];
            dp[i+1][j] += dp[i][j]*(1-p[i]);
        }
    }
    double ans = 0;
    REP(i, N+1){
        if (i > N-i){
            ans += dp[N][i];
        }
    }
    cout << fixed << setprecision(12);
    cout << ans << endl;
}