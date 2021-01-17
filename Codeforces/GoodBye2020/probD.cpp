#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N; cin >> N;
    vector<ll> W(N);
    ll S = 0ll;
    for (int i=0; i<N; i++) {
        cin >> W[i];
        S += W[i];
    }

    vector<int> G(N);
    for (int i=0; i<N-1; i++) {
        int a, b; cin >> a >> b;
        a--; b--;
        G[a]++;
        G[b]++;
    }

    vector<ll> P;
    for (int i=0; i<N; i++) {
        for (int j=0; j<G[i]-1; j++) {
            P.push_back(W[i]);
        }
    }

    sort(P.begin(), P.end(), greater<ll>());


    cout << S << " ";
    for (int i=0; i<N-2; i++) {
        
        S += P[i];
        cout << S << " ";
    }


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