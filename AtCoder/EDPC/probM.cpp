#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;
ll mod = 1E9+7;

int main() {
    int N, K; cin >> N >> K;
    int a[N]; REP(i, N) cin >> a[i];
    ll dp[N+1][K+1];
    REP(i, N+1) REP(j, K+1) dp[i][j] = 0;
    dp[0][0] = 1;
    REP(i, N){
        REP(j, K+1){
            dp[i+1][j] += dp[i][j];
            if (j+a[i]+1 <= K){
                dp[i+1][j+a[i]+1] -= dp[i][j];
            }
        }
        REP(j, K){
            dp[i+1][j+1] = (dp[i+1][j+1] + dp[i+1][j]) % mod;
            if (dp[i+1][j+1] < 0) dp[i+1][j+1] += mod;
        }
    }
    /*
    REP(i, N+1){
        REP(j, K+1){
            cout << dp[i][j] << ' ';
        }
        cout<< endl;
    }
    */
    cout << dp[N][K] << endl;
}