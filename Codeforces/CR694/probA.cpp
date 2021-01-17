#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N, M; cin >> M >> N;

    vector<int> K(M);
    vector<ll> C(N);
    for (int i=0; i<M; i++) {
        cin >> K[i];
        K[i]--;
    }
    for (int i=0; i<N; i++) {
        cin >> C[i];    
    }
    sort(K.begin(), K.end());
    vector<ll> A(M+1, 0ll);
    for (int i=0; i<M; i++) {
        A[i+1] = A[i] + C[K[i]];
    }
    ll ans = INFLL;
    ll t = 0ll;
    for (int i=0; i<min(N, M+1); i++) {
        if (K[M-i] < i) continue;
        ans = min(ans, t+A[M-i]);
        t += C[i];
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