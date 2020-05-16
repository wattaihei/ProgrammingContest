#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int T;
ll L[10000], R[10000];

ll solve(string A){
    int L = A.length();
    ll dp[L+1][4][2];
    REP(l, L+1) REP(i, 4) REP(isless, 2) dp[l][i][isless] = 0;
    dp[0][0][0] = 1;

    REP(l, L) REP(i, 4) REP(isless, 2){
        int a = A[l] - '0';
        REP(num, 10){
            if (num < a){
                if (num == 0){
                    dp[l+1][i][1] += dp[l][i][isless];
                }
                else if (i < 3){
                    dp[l+1][i+1][1] += dp[l][i][isless];
                }
            }
            else if (num == a || isless){
                if (num == 0){
                    dp[l+1][i][isless] += dp[l][i][isless];
                }
                else if (i < 3){
                    dp[l+1][i+1][isless] += dp[l][i][isless];
                }
            }
        }
    }
    ll ans = 0;
    REP(i, 4) ans += dp[L][i][0] + dp[L][i][1];
    return ans;
}

int main() {
    cin >> T;
    REP(i, T) cin >> L[i] >> R[i];
    REP(t, T){
        ll a1 = solve(to_string(L[t]-1));
        ll a2 = solve(to_string(R[t]));
        cout << a2 - a1 << endl;
    }
}