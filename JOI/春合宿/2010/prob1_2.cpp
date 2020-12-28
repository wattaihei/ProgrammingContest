#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    ll L; 
    int N; 
    cin >> L >> N;
    vector<set<ll>> X(2), Y(2);
    for (int i=0; i<N; i++) {
        ll x, y; cin >> x >> y;
        X[(int)(x+y)%2].insert(x-y);
        Y[(int)(x+y)%2].insert(x+y);
    }
    ll ans = 0ll;
    for (int i=0; i<2; i++) {
        vector<ll> B;
        for (ll x : X[i]) {
            ans += L-abs(x);
            B.push_back(x);
        }
        for (ll y : Y[i]) {
            ll s = L-abs(y+1-L);
            ans += s;
            ans -= (ll)(lower_bound(B.begin(), B.end(), s) - lower_bound(B.begin(), B.end(), -s));
        }
    }

    cout << ans << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}