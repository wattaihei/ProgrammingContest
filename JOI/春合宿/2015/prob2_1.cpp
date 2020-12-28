#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

const int MAXN = 1000000;

int N;
int B[MAXN];

void solve() {
    cin >> N;
    for (int i=0; i<N-1; i++) {
        cin >> B[i];
    }

    int only = 0, lastu = -1;
    int m = 0;
    ll ans = 0ll;
    for (int i=0; i<N-1; i++) {
        int d = B[i] - m;
        if (d > 2) {
            cout << 0 << endl;
            return;
        } else if (d == 2) {
            if (only > 0) {
                cout << 0 << endl;
                return;
            }
            only = i-lastu;
        }
        if (m < B[i]) {
            m = B[i];
            lastu = i;
        }
        ans += (ll)(m+1);
    }
    if (only) {
        cout << only << endl;
        return;
    }

    cout << ans - (N-2) << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}