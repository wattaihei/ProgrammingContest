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
    ll a, b, c, d; cin >> a >> b >> c >> d;
    ll m = (d-1)/(c-b);

    ll k = floor_sum(m+1, d, c, a) - floor_sum(m+1, d, b, a-1);
    cout << m-k << endl;
    
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