#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

pair<int, int> solve(vector<int> X) {
    int N = X.size();
    pair<int, int> p = {};
}

void solve() {
    int W, H, N;
    cin >> W >> H; cin >> N;
    vector<int> Xs, Ys;
    for (int i=0; i<N; i++) {
        int x, y; cin >> x >> y;
        Xs.push_back(x);
        Ys.push_back(y);
    }
    sort(Xs.begin(), Xs.end());
    sort(Ys.begin(), Ys.end());

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}