#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

int N;
int r, g, b, w;

bool solve(int r, int g, int b, int w) {
    if (r < 0 || g < 0 || b < 0) return false;
    int s = r%2 + g%2 + b%2;
    if (s + w%2 <= 1) return true;
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q; cin >> Q;
    for (int q=0; q<Q; q++) {
        //cin >> N;
        cin >> r >> g >> b >> w;
        cout << ((solve(r, g, b, w) || solve(r-1, g-1, b-1, w+3)) ? "Yes" : "No") << endl;
    }
}