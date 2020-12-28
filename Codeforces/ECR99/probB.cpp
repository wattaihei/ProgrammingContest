#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N; cin >> N;
    if (N == 1) {
        cout << 1 << endl;
        return;
    }
    int ans = INFINT;
    for (int i=2; i<=3000; i++) {
        int c = i*(i+1)/2;
        if (c == N) {
            ans = i;
            break;
        }
        else if (N < c-1) {
            ans = i;
            break;
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