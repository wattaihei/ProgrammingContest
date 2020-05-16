#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

ll INF = 100000000000000;
ll a, b, c;

int main() {
    ll N, M; cin >> N >> M;
    ll dp[N][N];
    REP(i, N) REP(j, N) dp[i][j] = INF;
    REP(i, M){
        cin >> a >> b >> c;
        if (c < dp[a-1][b-1]){
            dp[a-1][b-1] = c;
        }
        if (c < dp[b-1][a-1]){
            dp[b-1][a-1] = c;
        }
    }
    ll K; cin >> K;
    ll XYZ[K][3];
    REP(i, K){
        cin >> XYZ[i][0] >> XYZ[i][1] >> XYZ[i][2];
    }

    REP(k, N) REP(i, N) REP(j, N){
        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]);
    }
    REP(i, N) dp[i][i] = 0;
    ll x, y, z;
    REP(k, K){
        x = XYZ[k][0];
        y = XYZ[k][1];
        z = XYZ[k][2];
        REP(i, N) REP(j, N){
            dp[i][j] = min(dp[i][j], dp[i][x-1]+z+dp[y-1][j]);
            dp[i][j] = min(dp[i][j], dp[i][y-1]+z+dp[x-1][j]);
        }
        ll ans = 0;
        REP(i, N-1) FOR(j, i+1, N){
            ans += dp[i][j];
        }
        cout << ans << endl;
    }

}