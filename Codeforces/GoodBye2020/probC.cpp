#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    string S; cin >> S;

    int N = S.size();

    vector<int> change(N, 0);
    int ans = 0;
    for (int i=0; i<N; i++) {
        if (
            (i > 0 && S[i] == S[i-1] && change[i-1] == 0) ||
            (i > 1) && S[i] == S[i-2] && change[i-2] == 0
        ) {
            change[i] = 1;
            ans += 1;
        }
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