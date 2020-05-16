#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

ll mod = 1E9+7;

int main() {
    string K; cin >> K;
    int L = K.length();
    int D; cin >> D;

    ll dp[L+1][D][2];
    REP(i, L+1) REP(d, D) REP(k, 2) dp[i][d][k] = 0;
    dp[0][0][0] = 1;
    REP(l, L) REP(d, D) REP(isless, 2){
        int num = K[l] - '0';
        REP(next, 10){
            if (next < num) dp[l+1][(d+next)%D][1] += dp[l][d][isless];
            else if (next == num) dp[l+1][(d+next)%D][isless] += dp[l][d][isless];
            else{
                if (isless) dp[l+1][(d+next)%D][isless] += dp[l][d][isless];
            }
            dp[l+1][(d+next)%D][0] %= mod;
            dp[l+1][(d+next)%D][1] %= mod;
        }
    }
    ll ans = (dp[L][0][1] + dp[L][0][0] -1) % mod;
    if (ans < 0) ans += mod;
    cout << ans << endl;
}