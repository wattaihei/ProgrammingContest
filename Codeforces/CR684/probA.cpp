#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {

    int N, c0, c1, h; cin >> N >> c0 >> c1 >> h;
    string S; cin >> S;
    int zeros = 0;
    for (int i=0; i<N; i++) {
        if (S[i] == '0') {
            zeros++;
        }
    }
    int ans = INFINT;
    for (int z=0; z<=N; z++) {
        int cost = c0 * z + c1 * (N-z) + abs(z-zeros)*h;
        ans = min(ans, cost);
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