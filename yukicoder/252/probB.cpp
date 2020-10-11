#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int MAX = 10003;
ll INF = 10000000000;
//ll dp[1002][MAX+1];

int main() {
    int N; cin >> N;
    ll A[N+1];
    for (int i=0; i<N; i++){
        cin >> A[i];
    }
    ll dp[N+1][MAX+1];
    for (int i=0; i<N+1; i++){
        for (int j=0; j<MAX+1; j++){
            dp[i][j] = INF;
        }
    }
    dp[0][0] = 0ll;
    for (int i=0; i<N; i++){
        int a = A[i];
        ll k = INF;
        for (int j=0; j<MAX+1; j++){
            k = min(k, dp[i][j]);
            if (j < a){
                dp[i+1][j] = min(dp[i+1][j], k + (ll)(a-j));
            } else {
                dp[i+1][j] = min(dp[i+1][j], k + (ll)(j-a));
            }
        }
    }
    ll ans = INF;
    for (int j=0; j<MAX+1; j++){
        ans = min(ans, dp[N][j]);
        //cout << dp[N][j] << endl;
    }
    cout << ans << endl;


}