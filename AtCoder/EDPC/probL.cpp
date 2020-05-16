#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

int main() {
    int N; cin >> N;
    ll a[N]; REP(i, N) cin >> a[i];
    ll dp[N+1][N];
    REP(i, N) dp[1][i] = a[i];
    FOR(l, 2, N+1){
        REP(i, N-l+1){
            dp[l][i] = max(-dp[l-1][i+1] + a[i], -dp[l-1][i] + a[i+l-1]);
        }
    }
    cout << dp[N][0] << endl;
    
}