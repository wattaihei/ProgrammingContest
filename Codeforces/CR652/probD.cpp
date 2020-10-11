#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

const int MAX = 2000005;
const ll mod = 1000000007;

ll dp[MAX+1][2];
int Query[10101];

int main() {
    int Q; cin >> Q;
    for (int i=0; i<Q; i++){
        cin >> Query[i];
    }
    for (int i=0; i<4; i++){
        dp[i][0] = 0ll; dp[i][1] = 0ll;
    }
    for (int i=3; i<MAX; i++){
        if (i % 3 == 0){
            dp[i][0] = (dp[i-1][0] + 2 * dp[i-2][1]) % mod;
        } else if (i%3 == 1){
            dp[i][0] = (dp[i-1][1] + 2 * dp[i-2][0]) % mod;
        } else {
            dp[i][0] = (dp[i-1][1] + 2 * dp[i-2][1] ) % mod;
        }
        dp[i][1] = (dp[i-1][0] + 2 * dp[i-2][0] + 1ll) % mod;
    }

    ll ans;
    for (int i=0; i<Q; i++) {
        int n = Query[i];
        if (n%3 != 2){
            ans = dp[n][1]*4 % mod;
        } else {
            ans = dp[n][0]*4 % mod;
        }
        cout << ans << "\n";
    }
}