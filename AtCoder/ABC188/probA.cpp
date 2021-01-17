#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int x, y; cin >> x >> y;
    if (x < y) {
        swap(x, y);
    }
    cout << (x < y+3 ? "Yes" : "No") << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}