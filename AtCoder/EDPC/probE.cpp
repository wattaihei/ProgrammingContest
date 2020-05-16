#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N, W; cin >> N >> W;
    ll w[N], v[N];
    ll maxv = 0;
    for (int i=0; i<N; i++){
        cin >> w[i] >> v[i];
        maxv = max(maxv, v[i]);
    }
    maxv = maxv*N;
    ll INF = 1E12;
    ll dp[N+1][maxv+1];
    for (int i=0; i<=N; i++){
        dp[i][0] = 0;
        for (int j=1; j<=maxv; j++){
            dp[i][j] = INF;
        }
    }
    for (int i=0; i<N; i++){
        for (int j=0; j<=maxv; j++){
            if (j+v[i] > maxv){
                continue;
            }
            else{
                dp[i+1][j+v[i]] = min(dp[i+1][j+v[i]], dp[i][j] + w[i]);
            }
        }
        for (int j=0; j<=maxv; j++){
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]);
        }
    }

    ll ans = 0;
    for (int i=0; i<=maxv; i++){
        if (dp[N][i] <= W){
            ans = i;
        }
    }
    cout << ans << endl;
}