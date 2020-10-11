#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K;
    ll mod;
    cin >> N >> K >> mod;
    int MAX = (N/2)*(N/2+1)/2*K;
    //vector<vector<ll>> dp(N+1, vector<ll>(MAX+1, 0));
    ll dp[N+1][MAX+1];
    for (int n=0; n<=N; n++) {
        for (int k=0; k<=MAX; k++) {
            dp[n][k] = 0ll;
        }
    }
    dp[0][0] = 1ll;
    // int cnt = 0;
    for (int n=1; n<=N; n++) {
        vector<vector<ll>> Sum(n, {0ll});
        for (int k=0; k<=MAX; k++) {
            int l = Sum[k%n].size();
            ll a = (Sum[k%n][l-1] + dp[n-1][k]) % mod;
            if (l > K) {
                dp[n][k] = (a + mod - Sum[k%n][l-1-K]) % mod;
            } else {
                dp[n][k] = a;
            }
            Sum[k%n].push_back(a);
        }
    }
    vector<ll> P(N, 0ll);
    for (int n=1; n<=N/2+1; n++) {
        ll ans = 0ll;
        for (int k=1; k<=min((n-1)*n/2, (N-n)*(N-n+1)/2)*K; k++) {
            //cout << k << endl;
            ans = (ans + dp[n-1][k]*dp[N-n][k] % mod) % mod;
        }
        ans = ((ans * (ll)(K+1)) % mod + (ll)K) % mod;
        P[n-1] = ans;
        P[N-n] = ans;
    }
    for (ll a : P) {
        cout << a << "\n";
    }
    // cout << cnt << endl;
}