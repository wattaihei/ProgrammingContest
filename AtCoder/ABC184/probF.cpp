#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N; cin >> N;
    ll T; cin >> T;
    ll A[N];
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    vector<ll> Ss;
    for (int bit=0; bit<(1<<(N/2)); bit++) {
        ll s = 0ll;
        for (int i=0; i<N/2; i++) {
            if (bit&(1<<i)) {
                s += A[i];
            }
        }
        if (s <= T) {
            Ss.push_back(s);
        }
    }
    ll ans = 0ll;
    sort(Ss.begin(), Ss.end());
    for (int bit=0; bit<(1<<(N-(N/2))); bit++) {
        ll s = 0ll;
        for (int i=0; i<(N-(N/2)); i++) {
            if (bit&(1<<i)) {
                s += A[i+(N/2)];
            }
        }
        if (s > T) continue;
        // cout << s << endl;
        auto it = lower_bound(Ss.begin(), Ss.end(), T-s);
        if (it != Ss.end() && *it + s == T) {
            ans = T;
            break;
        } else {
            ans = max(ans, *(it-1) + s);
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