#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N, K; cin >> N >> K;
    vector<ll> A(N*K);
    for (int i=0; i<N*K; i++) {
        cin >> A[i];
    }
    reverse(A.begin(), A.end());
    int s = (N)/2+1;
    ll ans = 0ll;
    for (int i=0; i<K; i++) {
        ans += A[(i+1)*s-1];
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