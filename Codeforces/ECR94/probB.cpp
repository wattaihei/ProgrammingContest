#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        ll p, f; cin >> p >> f;
        ll maxx, maxy; cin >> maxx >> maxy;
        ll s, w; cin >> s >> w;
        ll ans = 0;
        for (ll x=0; x<=maxx; x++) {
            ll y = min(max(0ll, (p+f-s*x)/w), maxy);
            ans = max(ans, x+y);
        }
        cout << ans << endl;
    }
}