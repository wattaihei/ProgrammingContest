#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

const ll M = (1ll<<18);

void print(int query, ll ans) {
    cout << "Case #" << query+1 << ": ";
    cout << ans << endl;
}

void print_imp(int query) {
    cout << "Case #" << query+1 << ": IMPOSSIBLE" << endl;
}

ll s_to_ll(string sa) {
    ll a = 0ll;
    for (int i=0; i<sa.size(); i++) {
        if (sa[i] == '1') {
            a += (1ll<<(sa.size()-i-1));
        }
    }
    return a;
}

ll NOT(ll a) {
    if (a == 0) return 1;
    ll d = 0, b = a;
    while (b > 0) {
        b >>= 1;
        d++;
    }
    return (1ll<<d) - a - 1ll;
}

void solve(int query) {
    string sa, sb; cin >> sa >> sb;
    ll a = s_to_ll(sa), b = s_to_ll(sb);

    vector<ll> D(M, INFLL);
    D[a] = 0;
    queue<ll> q;
    q.push(a);
    while (!q.empty()) {
        ll p = q.front(); q.pop();
        vector<ll> nes = {NOT(p), p<<1};
        for (ll np : nes) {
            if (np < M && D[np] == INFLL) {
                D[np] = D[p] + 1;
                q.push(np);
            }
        }
    }

    if (D[b] == INFLL) {
        print_imp(query);
    } else {
        print(query, D[b]);
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        solve(q);
    }
}