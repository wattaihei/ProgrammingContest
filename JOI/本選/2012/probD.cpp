#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;

void solve() {
    int N, M; cin >> N >> M;
    vector<vector<int>> state(N+1);
    for (int i=0; i<N+1; i++) {
        vector<int> v(i+1, 0);
        state[i] = v;
    }
    for (int j=0; j<M; j++) {
        int x, y, a; cin >> x >> y >> a;
        x--; y--;
        state[x][y] = max(state[x][y], a+1);
    }
    int ans = 0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<i+1; j++) {
            int a = state[i][j];
            if (a > 0) ans++;
            state[i+1][j+1] = max(state[i+1][j+1], a-1);
            state[i+1][j] = max(state[i+1][j], a-1);
        }
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}