#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int solve() {
    int N; cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    vector<int> C(N+1, 0);
    ll ans = 0ll;
    for (int i=0; i<N; i++) {
        int a = A[i];
        ll s = 0;
        for (int j=i+1; j<N; j++) {
            int b = A[j];
            if (a == b) {
                ans += s;
            }
            s += (ll)C[b];
        }
        C[a]++;
    }
    cout << ans << endl;
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        solve();
    }
}