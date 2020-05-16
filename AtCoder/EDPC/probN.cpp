#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int main() {
    int N; cin >> N;
    ll a[N]; REP(i, N) cin >> a[i];
    ll sum[N][N];
    ll S;
    REP(l, N){
        S = 0;
        FOR(r, l, N){
            S += a[r];
            sum[l][r] = S;
        }
    }
    ll dp[N+1][N];
    REP(i, N) dp[1][i] = 0;
    FOR(l, 2, N+1){
        REP(i, N-l+1){
            ll tmp = dp[1][i] + dp[l-1][i+1];
            FOR(nl, 1, l){
                tmp = min(dp[nl][i] + dp[l-nl][i+nl], tmp);
            }
            dp[l][i] = tmp + sum[i][i+l-1];
        }
    }
    /*
    REP(l, N+1){
        REP(i, N){
            cout << dp[l][i] << ' ';
        }
        cout << endl;
    }
    */
    cout << dp[N][0] << endl;
}