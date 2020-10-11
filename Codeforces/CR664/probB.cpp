#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int n, m, x, y;

void solve() {
    cout << x << " " << y << endl; 
    for (int i=1; i<=n; i++) {
        if (i == x) continue;
        cout << i << " " << y << endl;
    }
    bool s = false;
    for (int j=1; j<=m; j++) {
        if (j == y) continue;
        if (s) {
            for (int i=1; i<=n; i++) {
                cout << i << " " << j << endl;
            }
            s = false;
        }
        else {
            for (int i=n; i>=1; i--) {
                cout << i << " " << j << endl;
            }
            s = true;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> m >> x >> y;
    solve();
}