#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int N;

// 6 10 14 15 21 
// 15 6 10 15 

void solve() {
    if (N > 6 + 10 + 14) {
        cout << "YES" << endl;
        if (N == (6+6+10+14)) {
            cout << 5 << " " << 6 << " " << 10 << " " << 15 << endl;
        } else if (N == (10+6+10+14)) {
            cout << 9 << " " << 6 << " " << 10 << " " << 15 << endl;
        } else if (N == (14+6+10+14)) {
            cout << 13 << " " << 6 << " " << 10 << " " << 15 << endl;
        } else {
            cout << 6 << " " << 10 << " " << 14 << " " << N-(6+10+14) << endl;
        }
        
    } else {
        cout << "NO" << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        cin >> N;
        solve();
    }
}