#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e16;

ll calc(vector<ll> X, ll L) {
    if (L > X[3] - X[0]) {
        return X[1] - X[0] + (X[0] + L - X[3]) + (X[0] + L - X[2]);
    }
    if (L <= X[2] - X[1]) {
        return X[3] - X[0] + X[2] - X[1] - 2*L;
    }
    return X[1] - X[0] + X[3] - X[2];
}

void solve() {
    vector<ll> X, Y;
    for (int i=0; i<4; i++) {
        ll x, y; cin >> x >> y;
        X.push_back(x);
        Y.push_back(y);
    }
    sort(X.begin(), X.end());
    sort(Y.begin(), Y.end());

    ll l1 = 0ll, r1 = INFLL, l2, r2;
    while (r1 - l1 > 4) {
        l2 = (2*l1+r1)/3;
        r2 = (l1+2*r1)/3;
        ll sl2 = calc(X, l2) + calc(Y, l2);
        ll sr2 = calc(X, r2) + calc(Y, r2);
        if (sl2 < sr2) {
            r1 = r2;
        } else {
            l1 = l2;
        }
    }

    ll ans = INFLL;
    for (ll l=max(l1-1,1ll); l<=r1+2; l++) {
        ans = min(ans, calc(X,l) + calc(Y,l));
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