#include <bits/stdc++.h>
typedef long long ll;
#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); i++)
using namespace std;

typedef tuple<ll, int, int, int> Tp;

struct edge {
    ll d;
    int n;
};

const int MAXN = 1e4;
const ll INF = 1e18;
int N, M, X;
int T[MAXN];
vector<edge> graph[MAXN];

ll solve() {
    ll Dist[N][X+1][3];
    for (int n=0; n<N; n++) {
        for (int x=0; x<X+1; x++){
            Dist[n][x][0] = INF;
            Dist[n][x][2] = INF;
        }
    }
    priority_queue<Tp, vector<Tp>, greater<Tp>> q;
    Dist[0][0][0] = 0ll;
    q.push({0ll, 0, 0, 0});
    ll d; int n, x, t;
    while (!q.empty()) {
        Tp p = q.top(); q.pop();
        d = get<0>(p);
        n = get<1>(p);
        x = get<2>(p);
        t = get<3>(p);
        if (Dist[n][x][t] < d) continue;
        //cout << n << " " << x << " " << t << " " << Dist[n][x][t] << endl;
        for (edge np : graph[n]) {
            if (T[np.n] == 1 || T[np.n] == t) {
                int nextx = T[np.n] == 1 ? min(x+(int)np.d, X) : 0;
                if (Dist[np.n][nextx][t] > Dist[n][x][t] + np.d) {
                    Dist[np.n][nextx][t] = Dist[n][x][t] + np.d;
                    q.push({Dist[np.n][nextx][t], np.n, nextx, t});
                }
            } else if (x + (int)np.d >= X) {
                if (Dist[np.n][0][T[np.n]] > Dist[n][x][t] + np.d) {
                    Dist[np.n][0][T[np.n]] = Dist[n][x][t] + np.d;
                    q.push({Dist[np.n][0][T[np.n]], np.n, 0, T[np.n]});
                }
            }
        }
    }
    ll ans = INF;
    for (int x=0; x<X+1; x++) {
        ans = min(ans, Dist[N-1][x][0]);
        ans = min(ans, Dist[N-1][x][2]);
    }
    return ans;
}

int main() {
    cin >> N >> M >> X;
    for (int i=0; i<N; i++) {
        cin >> T[i];
    }
    for (int m=0; m<M; m++) {
        int a, b, d;
        cin >> a >> b >> d;
        graph[a-1].push_back({d, b-1});
        graph[b-1].push_back({d, a-1});
    }
    cout << solve() << endl;
}