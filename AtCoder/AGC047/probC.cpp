#include <bits/stdc++.h>
#include <atcoder/convolution>
#include <atcoder/modint>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;
using namespace atcoder;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {

    ll P = 200003ll;
    vector<ll> twoind_to_val(P, 0ll), val_to_twoind(P, 0ll), V(P, 0ll);

    ll b = 1;
    for (int i=0; i<P; i++) {
        twoind_to_val[i] = b;
        val_to_twoind[b] = i;
        b = b * 2 % P;
    }

    int N; cin >> N;
    for (int i=0; i<N; i++) {
        ll a; cin >> a;
        if ( a == 0ll) continue;
        V[val_to_twoind[a]]++;
    }

    vector<ll> X = convolution_ll(V, V);

    ll ans = 0ll;
    for (int i=0; i<2*P; i++) {
        ans += twoind_to_val[i%P] * X[i];
        if (i%2 == 0) {
            ll v = V[i/2];
            ans -= twoind_to_val[i%P] * v*(v-1)/2;
        }
    }

    cout << (ans / 2) << endl;
    
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}