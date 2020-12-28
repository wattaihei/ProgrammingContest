#include <bits/stdc++.h>
#include <atcoder/math>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;
using namespace atcoder;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    ll n, s, k;
    cin >> n >> s >> k;
    ll g = gcd(gcd(n, k), s);
    n /= g;
    k /= g;
    s /= g;
    g = gcd(n, k);
    if (g != 1) {
        cout << -1 << endl;
        return;
    }
    ll b = (n-s)*inv_mod(k, n);
    auto x = crt({b%n}, {n});
    ll y = x.first, z = x.second;
    ll ans = y*g % z;
    if ((y == 0 && z == 0)) {
        cout << -1 << endl;
        return;
    }
    cout << ans << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        solve();
    }
}