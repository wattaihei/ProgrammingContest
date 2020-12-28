#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 2e18;


struct node {
    ll d;
    int i, s;
};

class comp {
    public:
    bool operator() (node a, node b) {
        return a.d > b.d;
    }
};

void solve() {
    int M, N, Q; cin >> M >> N >> Q;
    vector<vector<vector<int>>> XY(2, vector<vector<int>>(max(M,N)+1));
    vector<vector<int>> Points(2, vector<int>(Q+2));
    for (int iq=0; iq<Q+2; iq++) {
        int x, y;
        if (iq < Q) {
            cin >> x >> y;
        } else if (iq == Q) {
            x = 1; y = 1;
        } else {
            x = M; y = N;
        }
        XY[0][x].push_back(iq);
        XY[1][y].push_back(iq);
        Points[0][iq] = x;
        Points[1][iq] = y;
    }

    vector<vector<ll>> D(2, vector<ll>(Q+2, INFLL));
    priority_queue<node, vector<node>, comp> q;
    q.push({0ll, Q, 0});
    D[0][Q] = 0ll;
    while (!q.empty()) {
        node p = q.top(); q.pop();
        if (D[p.s][p.i] < p.d) continue;
        for (int ni : XY[p.s][Points[p.s][p.i]]) {
            ll d = D[p.s][p.i] + (ll)abs(Points[p.s^1][p.i]-Points[p.s^1][ni]);
            if (d < D[p.s][ni]) {
                D[p.s][ni] = d;
                q.push({d, ni, p.s});
            }
        }
        if (p.i != Q && D[p.s^1][p.i] > D[p.s][p.i] + 1ll) {
            D[p.s^1][p.i] = D[p.s][p.i] + 1ll;
            q.push({D[p.s^1][p.i], p.i, p.s^1});
        }
    }

    ll ans = min(D[0][Q+1], D[1][Q+1]);
    cout << (ans == INFLL ? -1 : ans) << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}