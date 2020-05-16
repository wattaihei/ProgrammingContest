#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    int N, W; cin >> N >> W;
    ll w[N], v[N];
    for (int i=0; i<N; i++){
        cin >> w[i] >> v[i];
    }
    ll dp[N+1][W+1];
    for (int i=0; i<=W; i++){
        dp[0][i] = 0;
    }
    for (int i=0; i<N; i++){
        for (int j=0; j<=W; j++){
            if (j-w[i] < 0){
                dp[i+1][j] = dp[i][j];
            }
            else{
                dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i]);
            }
        }
    }
    cout << dp[N][W] << endl;
}