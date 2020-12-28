#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
#define endl "\n";
using namespace std;

const int INFINT = 2e9;
const ll INFLL = 1e18;

struct edge {
    ll t, h;
    int p;
};

const int MAXN = 100000;

int N, M;
ll X;
ll H[MAXN];
vector<edge> graph[MAXN];

class comp {
    public:
    bool operator()(edge a, edge b) {
        return a.t > b.t;
    }
};


void solve() {
    cin >> N >> M >> X;
    for (int i=0; i<N; i++) {
        cin >> H[i];
    }
    for (int i=0; i<M; i++) {
        int a, b;
        ll t;
        cin >> a >> b >> t;
        graph[a-1].push_back({t, 0, b-1});
        graph[b-1].push_back({t, 0, a-1});
    }

    vector<ll> D(N, INFLL), Height(N, INFLL);
    priority_queue<edge, vector<edge>, comp> q;
    D[0] = 0;
    Height[0] = X;
    q.push({0, X, 0});
    while (!q.empty()) {
        edge e = q.top(); q.pop();
        if (e.t > D[e.p] + abs(Height[e.p]-e.h)) {
            continue;
        }
        for (edge ne : graph[e.p]) {
            ll nh, nd;
            if (H[e.p] < ne.t) {
                // 届かない
                continue;
            }
            if (Height[e.p] - ne.t < 0) {
                nh = 0;
                nd = D[e.p] + 2*ne.t - Height[e.p];
            } else if (Height[e.p] - ne.t > H[ne.p]) {
                nh = H[ne.p];
                nd = D[e.p] + (Height[e.p] - H[ne.p]);
            } else {
                nh = Height[e.p] - ne.t;
                nd = D[e.p] + ne.t;
            }
            if (nd < D[ne.p] + abs(Height[ne.p] - nh)) {
                D[ne.p] = nd;
                Height[ne.p] = nh;
                q.push({nd, nh, ne.p});
            }
        }
    }

    cout << (D[N-1] == INFLL ? -1 : D[N-1] + (H[N-1]-Height[N-1])) << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}